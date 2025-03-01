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
            
            
            
class Pitcher(Conversable):
    def __init__(self, name, revenue, growth_rate, valuation, equity_asked, scalability, conviction):
        """
        Initialize a Pitcher with business details.
        
        Args:
        - name (str): The name of the Pitcher.
        - revenue (float): The revenue the startup has generated.
        - growth_rate (float): Projected growth rate (percentage increase) for the next year.
        - valuation (float): The current valuation of the startup.
        - equity_asked (float): The percentage of equity the Pitcher is offering.
        - scalability (bool): Whether the business is scalable.
        - conviction (int): The Pitcher's conviction level (scale of 1-10).
        """
        super().__init__(name, role="Pitcher")
        self.revenue = revenue
        self.growth_rate = growth_rate
        self.valuation = valuation
        self.equity_asked = equity_asked
        self.scalability = scalability
        self.conviction = conviction
        
        
    def introduce_business(self):
        """Simulate the Pitcher's introduction of their business."""
        message = f"Hi Sharks, I am {self.name}, the founder of my company. Our current revenue is ${self.revenue}, and we're growing at a rate of {self.growth_rate*100}% annually. " \
                  f"Our valuation is ${self.valuation}, and I’m offering {self.equity_asked}% equity. The business is scalable and we're looking to expand."
        self.send_message(message)
        return message  
    
    
    def answer_question(self, question):
        """Simulate the Pitcher's responses to the Sharks' questions."""
        if "scalability" in question.lower():
            return "Yes, our business model is designed to scale rapidly in new markets."
        elif "valuation" in question.lower():
            return f"Our valuation is based on the growth potential and market opportunity. We're seeing a strong demand in our industry."
        elif "revenue" in question.lower():
            return f"Our revenue is growing steadily, and we’re expecting to hit $2 million by the end of this year."
        else:
            return "We have a strong business plan and are confident in our growth."
        
        
        
class Shark(Conversable):
    def __init__(self, name, conviction_factor=1):
        """
        Initialize a Shark with decision-making characteristics.
        
        Args:
        - name (str): The name of the Shark.
        - conviction_factor (float): A factor representing the Shark's flexibility and interest in a deal (default is 1).
        """
        super().__init__(name, role="Shark")
        self.conviction_factor = conviction_factor
        
        
    def ask_question(self, pitcher):
        """Simulate the Shark asking a question to the Pitcher."""
        questions = [
            "What is your scalability plan?",
            "How did you arrive at your current valuation?",
            "What are your revenue projections for the next year?",
            "What makes your business unique compared to competitors?"
        ]
        question = random.choice(questions)
        self.send_message(question)
        return question

    def evaluate_pitcher(self, pitcher):
        """Evaluates the Pitcher's startup based on business details and returns a decision (Offer, Counteroffer, Decline)."""
        score = self._evaluate_pitcher(pitcher)
        if score >= 70:
            return "Offer", score
        elif score >= 50:
            return "Counteroffer", score
        else:
            return "Decline", score
        
        
    def _evaluate_pitcher(self, pitcher):
        """Private method that calculates the score based on various evaluation criteria."""
        score = 0

        # Factor 1: Revenue
        if pitcher.revenue > 1_000_000:
            score += 30
        else:
            score += 10

        # Factor 2: Growth Rate
        if pitcher.growth_rate > 0.5:
            score += 20
        else:
            score += 5

        # Factor 3: Valuation vs Revenue
        if pitcher.valuation / pitcher.revenue < 10:
            score += 15
        else:
            score -= 10

        # Factor 4: Scalability
        if pitcher.scalability:
            score += 20

        # Factor 5: Conviction
        if pitcher.conviction >= 8:
            score += 10
        else:
            score += 5

        # Apply the Shark's conviction factor to their decision
        score *= self.conviction_factor

        return score