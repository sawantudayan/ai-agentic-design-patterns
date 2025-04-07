# Conversational Chess with AI Agents

This usecase demonstrates a conversational chess game between two AI agents, "Player White" and "Player Black", using
the tools and functionalities provided by the autogen library. The chessboard state is managed with the chess library,
and each agent interacts to make moves using defined tools.

# Setup

To set up this notebook, we need to initialize the necessary libraries, configurations, and the chessboard state.

## Install Dependencies:

- The core libraries required are:
    - ```chess```: for chess game logic.
    - ```autogen```: to manage agent interactions and tool usage.

## Initialize the Chess Board:

- A chessboard instance is created using ```chess.Board()```.
- We initialize the variable ```made_move``` to track if a move has been made.

## Agent Creation & Configuration

In this section, we create the AI agents responsible for playing chess, managing the conversation, and making moves on
the chessboard.

- Player White Agent:
    - This agent represents the white player. It can request legal moves and make a move using the
      ```get_legal_moves()``` and
      ```make_move()``` tools.
- Player Black Agent:
    - This agent represents the black player, configured similarly to the white player but as the second participant in
      the chess game.
- Board Proxy Agent:
    - The ```Board Proxy``` agent handles the communication between the players and is responsible for updating the
      board and controlling the game flow.

## Creation & Execution

This section covers the tools and the game logic that manage the chess game interaction.

- Tool Creation:
    - Tool for Getting Legal Moves: This tool provides a list of legal moves in UCI format from the current board state.
    - Tool for Making a Move: This tool allows a player to make a move on the chessboard. It also displays the updated
      board after each move.
- Registering Tools: The tools ````(get_legal_moves and make_move)```` are registered for both the white and black
  agents.
- Registering Nested Chats: Nested chats are registered between the agents, which will trigger one another based on
  their moves.

## Structure for Each Agent

Each agent follows a similar structure, as outlined below:

- Agent Name: Specifies the agent's role (e.g., "Player White", "Player Black").
- System Message: Defines the agent's behavior and instructions on how it should interact with the chessboard and other
  agents.
- LLM Configuration: Configuration for the large language model, indicating which tools the agent can use.

## Contributors

Udayan Sawant - Creator and Developer