# AI Agentic Design Patterns with AutoGen

# [Shark Tank Simulation](https://github.com/sawantudayan/ai-agentic-design-patterns/tree/feature1/multi_agent_conversation/multi_agent_conversation/shark_tank_simulator)

This ```usecase``` simulates a Shark Tank-style negotiation between a **Pitcher** (entrepreneur) and a **Panel of Sharks
** (
investors). It dynamically handles business pitches, investor responses, and deal-making negotiations based on
pre-defined evaluation criteria.

## Features

- **Pitcher Introduction**: The pitcher presents their startup, explaining the problem it solves, their sales, revenue,
  capital table, and the equity shares they are offering.
- **Shark Panel Evaluation**: The sharks ask probing questions and evaluate the pitch based on the pitcher’s
  projections, valuation, growth potential, and scalability.
- **Negotiations**: Sharks may make counter-offers or close a deal based on factors like:
    - Revenue and scalability of the business.
    - Equity asked vs. business valuation.
    - The pitcher’s conviction and vision for scaling the business.
- **Dynamic Data Input**: The simulation can be run with dynamic data loaded from a JSON file or hardcoded values. Data
  can be read from an `.env` file to dynamically set the path for the JSON.
- **Multiple Scenarios**: Sharks may make different decisions based on the evaluation, with various negotiation
  outcomes (offers, counteroffers, or rejection).

# [Customer Onboarding Agent](https://github.com/sawantudayan/ai-agentic-design-patterns/tree/feature2/sequential_chats)

This ```usecase``` demonstrates the process of simulating sequential interactions between AI agents to facilitate
customer
onboarding. It walks through the setup, creation of agents, tasks, and initiating the customer onboarding process.

## Features

**Conversable Agent Setup**: Multiple conversational agents are created using the ConversableAgent class from autogen.

- **Onboarding Personal Information Agent**: This agent interacts with the customer to gather their name and location.
  It is
  specifically configured to ask only for personal information, with termination occurring once the data is gathered.
- **Onboarding Topic Preference Agent**: This agent collects customer preferences related to news topics they are
  interested
  in.
- **Customer Engagement Agent**: This agent creates an engaging experience by suggesting fun content such as jokes,
  stories,
  or facts based on the customer's preferences.

**Customer Proxy Agent**: Acts as an intermediary, receiving messages from the agents and enabling the conversation flow
with the customer.