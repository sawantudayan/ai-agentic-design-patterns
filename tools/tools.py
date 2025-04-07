import chess
import chess.svg
from autogen import ConversableAgent, register_function
from typing_extensions import Annotated


# Chess Game Class to handle the board and moves
class ChessGame:
    def __init__(self):
        self.board = chess.Board()
        self.made_move = False

    def get_legal_moves(self) -> Annotated[str, "A list of legal moves in UCI format"]:
        return "Possible moves are: " + ",".join([str(move) for move in self.board.legal_moves])

    def make_move(self, move: Annotated[str, "A move in UCI format."]) -> Annotated[str, "Result of the move."]:
        move = chess.Move.from_uci(move)
        self.board.push_uci(str(move))
        self.made_move = True

        # Display the board.
        display(
            chess.svg.board(
                self.board,
                arrows=[(move.from_square, move.to_square)],
                fill={move.from_square: "gray"},
                size=200,
            )
        )

        # Get the piece name.
        piece = self.board.piece_at(move.to_square)
        piece_symbol = piece.unicode_symbol()
        piece_name = (
            chess.piece_name(piece.piece_type).capitalize()
            if piece_symbol.isupper()
            else chess.piece_name(piece.piece_type)
        )

        return f"Moved {piece_name} ({piece_symbol}) from {chess.SQUARE_NAMES[move.from_square]} to {chess.SQUARE_NAMES[move.to_square]}."

    def check_made_move(self) -> bool:
        if self.made_move:
            self.made_move = False
            return True
        else:
            return False


# Agent Class for Managing Players
class ChessPlayerAgent:
    def __init__(self, name: str, system_message: str, llm_config: dict):
        self.agent = ConversableAgent(
            name=name,
            system_message=system_message,
            llm_config=llm_config,
        )

    def register_tools(self, game: ChessGame):
        register_function(
            game.get_legal_moves,
            caller=self.agent,
            executor=board_proxy,
            name="get_legal_moves",
            description="Get legal moves.",
        )

        register_function(
            game.make_move,
            caller=self.agent,
            executor=board_proxy,
            name="make_move",
            description="Call this tool to make a move.",
        )

    def register_nested_chats(self, other_agent, board_proxy):
        self.agent.register_nested_chats(
            trigger=other_agent.agent,
            chat_queue=[
                {
                    "sender": board_proxy,
                    "recipient": self.agent,
                    "summary_method": "last_msg",
                }
            ],
        )


# Board Proxy Agent Class
class BoardProxyAgent:
    def __init__(self, check_made_move_func):
        self.agent = ConversableAgent(
            name="Board Proxy",
            llm_config=False,
            is_termination_msg=check_made_move_func,
            default_auto_reply="Please make a move.",
            human_input_mode="NEVER",
        )


# Chess Game Orchestration Class
class ChessGameOrchestrator:
    def __init__(self, llm_config):
        self.llm_config = llm_config
        self.game = ChessGame()
        self.board_proxy = BoardProxyAgent(self.game.check_made_move)
        self.player_white = ChessPlayerAgent(
            "Player White",
            "You are a chess player and you play as white. First call get_legal_moves(), to get a list of legal moves. Then call make_move(move) to make a move.",
            llm_config,
        )
        self.player_black = ChessPlayerAgent(
            "Player Black",
            "You are a chess player and you play as black. First call get_legal_moves(), to get a list of legal moves. Then call make_move(move) to make a move.",
            llm_config,
        )

    def setup_agents(self):
        # Register tools for both players
        self.player_white.register_tools(self.game)
        self.player_black.register_tools(self.game)

        # Register nested chats between the two players
        self.player_white.register_nested_chats(self.player_black, self.board_proxy)
        self.player_black.register_nested_chats(self.player_white, self.board_proxy)

    def start_game(self):
        # Initiate the game by having player black make the first move
        chat_result = self.player_black.agent.initiate_chat(
            self.player_white.agent,
            message="Let's play chess! Your move.",
            max_turns=2,
        )
        return chat_result


# Main function to initialize and start the game
def main():
    llm_config = {"model": "gpt-4-turbo"}

    # Initialize the game orchestrator
    orchestrator = ChessGameOrchestrator(llm_config)

    # Set up the agents and tools
    orchestrator.setup_agents()

    # Start the game and initiate chat
    chat_result = orchestrator.start_game()

    # Print the result of the game initiation
    print(chat_result)


if __name__ == "__main__":
    main()
