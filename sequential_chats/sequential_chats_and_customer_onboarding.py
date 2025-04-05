class ConversableAgent:
    def __init__(self, name, system_message, llm_config, human_input_mode="NEVER"):
        self.name = name
        self.system_message = system_message
        self.llm_config = llm_config
        self.human_input_mode = human_input_mode

    def communicate(self, message):
        """
        Method to simulate agent's communication with the customer.
        Returns a simulated response based on the agent's role.
        """
        print(f"{self.name} says: {message}")

    def gather_info(self, info_type):
        """
        Simulates gathering customer information. Returns data as a dictionary.
        """
        if info_type == "personal":
            return {"name": "John Doe", "location": "New York"}
        elif info_type == "topic":
            return {"topics": ["Technology", "Science", "Sports"]}
        return {}

    def terminate(self):
        print(f"{self.name} has completed its task and is terminating.")
        return "TERMINATE"


class OnboardingPersonalInformationAgent(ConversableAgent):
    def __init__(self, llm_config):
        super().__init__(
            name="Onboarding Personal Information Agent",
            system_message="You are a helpful customer onboarding agent, gathering name and location.",
            llm_config=llm_config
        )

    def run(self):
        # Simulate gathering name and location from the customer
        self.communicate("Could you tell me your name and location?")
        customer_info = self.gather_info("personal")
        return customer_info


class OnboardingTopicPreferenceAgent(ConversableAgent):
    def __init__(self, llm_config):
        super().__init__(
            name="Onboarding Topic Preference Agent",
            system_message="You are a helpful customer onboarding agent, gathering topic preferences.",
            llm_config=llm_config
        )

    def run(self):
        # Simulate gathering topic preferences from the customer
        self.communicate("Could you tell me what topics you are interested in?")
        topic_preferences = self.gather_info("topic")
        return topic_preferences


class CustomerEngagementAgent(ConversableAgent):
    def __init__(self, llm_config):
        super().__init__(
            name="Customer Engagement Agent",
            system_message="You are a fun customer engagement agent, providing engaging content.",
            llm_config=llm_config
        )

    def run(self, customer_info, topic_preferences):
        # Simulate providing fun content based on customer info and preferences
        self.communicate(
            f"Let's find something fun for you to read based on your interests in {', '.join(topic_preferences['topics'])}.")
        return "Here is a fun fact about technology!"


class CustomerProxyAgent:
    def __init__(self):
        self.conversation_history = []

    def receive_message(self, sender, message):
        self.conversation_history.append((sender.name, message))
        print(f"Customer Proxy received message from {sender.name}: {message}")

    def send_message(self, recipient, message):
        recipient.communicate(message)

    def start_conversation(self, agent_sequence):
        for agent in agent_sequence:
            if isinstance(agent, ConversableAgent):
                self.receive_message(agent, agent.system_message)
                if agent.name == "Onboarding Personal Information Agent":
                    customer_info = agent.run()
                    self.send_message(agent, f"Received: {customer_info}")
                elif agent.name == "Onboarding Topic Preference Agent":
                    topic_preferences = agent.run()
                    self.send_message(agent, f"Received: {topic_preferences}")
                elif agent.name == "Customer Engagement Agent":
                    fun_content = agent.run(customer_info, topic_preferences)
                    self.send_message(agent, f"Enjoy: {fun_content}")


# Setting up the LLM config
llm_config = {"model": "gpt-3.5-turbo"}

# Creating agent instances
personal_info_agent = OnboardingPersonalInformationAgent(llm_config)
topic_preference_agent = OnboardingTopicPreferenceAgent(llm_config)
engagement_agent = CustomerEngagementAgent(llm_config)

# Create a customer proxy to handle communication
customer_proxy = CustomerProxyAgent()

# Initiate the onboarding process with sequential tasks
customer_proxy.start_conversation([personal_info_agent, topic_preference_agent, engagement_agent])
