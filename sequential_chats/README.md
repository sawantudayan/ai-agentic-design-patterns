# Usecase 2: Sequential Chats & Customer Onboarding

This usecase demonstrates the process of simulating sequential interactions between AI agents to facilitate customer
onboarding. It walks through the setup, creation of agents, tasks, and initiating the customer onboarding process.

## Setup

- LLM Configuration: It sets up the configuration for the language model to use gpt-3.5-turbo.
- Package Installation: Installs the autogen package to enable AI-driven agent interactions.

## Agent Creation and Configuration

Conversable Agent Setup: Multiple conversational agents are created using the ConversableAgent class from autogen.

- Onboarding Personal Information Agent: This agent interacts with the customer to gather their name and location. It is
  specifically configured to ask only for personal information, with termination occurring once the data is gathered.
- Onboarding Topic Preference Agent: This agent collects customer preferences related to news topics they are interested
  in.
- Customer Engagement Agent: This agent creates an engaging experience by suggesting fun content such as jokes, stories,
  or facts based on the customer's preferences.

Customer Proxy Agent: Acts as an intermediary, receiving messages from the agents and enabling the conversation flow
with the customer.

## Task Creation and Execution

- Sequential Task Flow: The notebook defines a series of tasks, where agents communicate in a structured manner:
    - Personal Information Task: The personal information agent asks for the customer's name and location.
    - Topic Preference Task: The topic preference agent queries the customer for their interests in news topics.
    - Engagement Task: The engagement agent provides interactive content based on the customer's profile.

- Message Exchange: Tasks are defined by specifying sender-receiver pairs, messages, and conditions for summary and
  termination.

## Sequential Chat Execution

- **Initiating Chats**: The initiate_chats function starts the sequence of conversations between the customer and the
  agents, ensuring each agent completes its task before passing the interaction along.
- **Summary and Cost Output**: After each conversation, a summary is generated, and the cost of the interaction is
  printed. This allows for monitoring of both the conversation quality and resource utilization.

## Clear Structure for Each Agent's Role

- Each agent is tailored to a specific part of the customer onboarding process, ensuring clarity and structure in the
  interaction flow.
- The agents are configured to operate autonomously, ensuring minimal human input (human_input_mode="NEVER"), but
  flexibility for customer interactions via the customer proxy agent.

## Termination Conditions

Each agent has termination conditions built in. For instance, the customer engagement agent terminates the conversation
once it has fulfilled its role, and each agent automatically terminates after completing its task.

## Simple Integration and Customization

- The setup allows for easy addition of new agents, tasks, and functionalities to enhance the customer onboarding
  process.
- Agents can be modified or extended with different system messages or tasks depending on the specific requirements of
  the customer service or onboarding process.

## Contributors

Udayan Sawant - Creator and Developer