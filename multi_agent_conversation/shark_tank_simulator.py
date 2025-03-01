import random

class Conversable:
    def __init__(self, name, role):
        """
            Initialize a Conversable agent (either a Pitcher or a Shark) that can communicate.
        
            Args:
                - name (str): The name of the agent.
                - role (str): The role of the agent (e.g., "Pitcher" or "Shark").
        """
        self.name = name
        self.role = role
        self.chat_history = []  # History of the conversation
        
        
    def send_message(self, message):
        """
            Simulates the agent sending a message.
        
            Args:
                - message (str): The message being sent.
        """
        self.chat_history.append({"role": self.role, "message": message})
        
        
    def receive_message(self, message):
        """
            Simulates the agent receiving a message.
        
            Args:
                - message (str): The message received from the other agent.
        """
        self.chat_history.append({"role": "Other", "message": message})

    
    def show_chat_history(self):
        """Displays the conversation history."""
        for entry in self.chat_history:
            print(f"{entry['role']}: {entry['message']}")