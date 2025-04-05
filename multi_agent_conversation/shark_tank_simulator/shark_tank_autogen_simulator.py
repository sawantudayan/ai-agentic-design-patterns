import openai
from autogen import ConversableAgent
from dotenv import load_dotenv
import os
import json



# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")


# Setup for the Pitcher and Sharks
class SharkTankSimulation:
    def __init__(self, pitcher_data, sharks_data):
        self.pitcher_data = pitcher_data
        self.sharks_data = sharks_data
        
        
    def setup_pitcher(self):
        # Safely use data with fallback defaults
        name = self.pitcher_data.get('name', 'Unknown Pitcher')
        company = self.pitcher_data.get('company', 'Unknown Company')
        revenue = self.pitcher_data.get('revenue', 0)
        growth_rate = self.pitcher_data.get('growth_rate', 0)
        valuation = self.pitcher_data.get('valuation', 0)
        equity_asked = self.pitcher_data.get('equity_asked', 0)
        scalability = self.pitcher_data.get('scalability', False)
        conviction = self.pitcher_data.get('conviction', 0)

        business_summary = (f"We are {company}, a startup generating {revenue} in revenue with a growth rate of {growth_rate * 100}%."
                            f" We are seeking {equity_asked}% equity for {valuation} valuation. "
                            f"Our business is {'scalable' if scalability else 'not scalable'}, and we are passionate about our vision.")
        
        self.pitcher = ConversableAgent(
            name="Pitcher",
            system_message=f"You are an entrepreneur presenting your startup. {business_summary}",
            #llm_config={'model': "text-embedding-3-small"}, # token limits: 40,000TPM, request & other limits:100RPM & 2,000 RPD
            llm_config={'model': "gpt-3.5-turbo"}, # token limits: 40,000TPM, request & other limits:3RPM & 200 RPD
            human_input_mode="NEVER"
        )
        
            
            
    def setup_sharks(self):
        self.sharks = []
        for shark in self.sharks_data:
            # Safely get shark system messages and conviction factor
            system_message = shark.get('system_message', 'You are a Shark investor evaluating a pitch.')
            conviction_factor = shark.get('conviction_factor', 0)

            shark_agent = ConversableAgent(
                name=shark['name'],
                system_message=system_message,
                #llm_config={'model': "text-embedding-3-small"}, # token limits: 40,000TPM, request & other limits:100RPM & 2,000 RPD
                llm_config={'model': "gpt-3.5-turbo"}, # token limits: 40,000TPM, request & other limits:3RPM & 200 RPD
                human_input_mode="NEVER"
            )
            shark_agent.conviction_factor = conviction_factor  # Attach the conviction factor
            self.sharks.append(shark_agent)
          

  
    def load_simulation_data(self, json_file):
        """Load simulation data from a JSON file."""
        with open(json_file, 'r') as file:
            data = json.load(file)
        self.pitcher_data = data['pitcher']
        self.sharks_data = data['sharks']
        
    

    def run_simulation(self):
        """Run the multi-agent Shark Tank simulation."""
        self.setup_pitcher()
        self.setup_sharks()

        # Create the initial pitch message
        pitcher_message = f"Hello Sharks, I am {self.pitcher_data.get('name', 'Unknown Pitcher')} from {self.pitcher_data.get('company', 'Unknown Company')} and I am seeking {self.pitcher_data.get('equity_asked', 'Not specified')}% equity for {self.pitcher_data.get('valuation', 'Not specified')} valuation. {self.pitcher_data.get('business_summary', 'No business summary provided.')}"

        # Send the initial pitch to all sharks
        for shark in self.sharks:
            chat_result = shark.initiate_chat(
                recipient=self.pitcher,
                message=pitcher_message,
                max_turns=5
            )
            print(f"Shark {shark.name} initial response:")
            print(chat_result.chat_history)
        
        # Sharks ask questions and evaluate the pitch
        for shark in self.sharks:
            question = f"Can you tell me more about {self.pitcher_data.get('name', 'Unknown Pitcher')}'s revenue and future projections?"
            chat_result = shark.initiate_chat(
                recipient=self.pitcher,
                message=question,
                max_turns=5
            )
            print(f"Shark {shark.name} questions the pitcher:")
            print(chat_result.chat_history)

        # Decision-making based on evaluation criteria
        self.evaluate_deals()
        

    def evaluate_deals(self):
        """Simulate the decision-making process of each Shark."""
        for shark in self.sharks:
            decision = self.shark_evaluation(shark)
            if decision == 'invest':
                print(f"Shark {shark.name} decides to invest!")
            elif decision == 'counter':
                print(f"Shark {shark.name} makes a counteroffer!")
            else:
                print(f"Shark {shark.name} decides not to invest.")
                
                
    def shark_evaluation(self, shark):
        """Evaluate each shark's decision-making criteria."""
        # Evaluation criteria
        pitcher_revenue = self.pitcher_data.get('revenue', 0)
        pitcher_valuation = self.pitcher_data.get('valuation', 0)
        pitcher_conviction = self.pitcher_data.get('conviction', 0)
        shark_conviction_factor = shark.conviction_factor
        
        # Example criteria: if revenue is high and business is scalable, sharks are more likely to invest
        if pitcher_revenue >= 1000000 and self.pitcher_data.get('scalability', False):
            investment_probability = (pitcher_conviction + shark_conviction_factor) / 2
            if investment_probability >= 0.75:
                return 'invest'  # Interested to invest
        # If the valuation is too high compared to revenue, they may counter
        elif pitcher_valuation > 10 * pitcher_revenue:
            return 'counter'  # Unreasonable valuation, will make a counteroffer
        else:
            return 'reject'  # Not investing
        
        
# Function to load the simulation data from JSON using the environment variable for the file path
def load_simulation_data_from_json():
    """Load pitcher and sharks data from a JSON file."""
    # Get the file path from the environment variable
    json_file = os.getenv('SHARK_TANK_JSON_PATH')
    print(f"Loading simulation data from: {json_file}")  # Debug output
    
    if not json_file:
        raise ValueError("SHARK_TANK_JSON_PATH environment variable not set.")
    
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file at {json_file} does not exist.")
        raise
    return data['pitcher'], data['sharks']


# Load the simulation data from a JSON file using the path from the environment variable
try:
    pitcher_data, sharks_data = load_simulation_data_from_json()
except Exception as e:
    print(e)
    exit(1)

# Initialize and run the Shark Tank simulation
simulation = SharkTankSimulation(pitcher_data, sharks_data)
simulation.run_simulation()