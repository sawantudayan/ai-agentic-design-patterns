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

# [Reflection Framework Use Case](https://github.com/sawantudayan/ai-agentic-design-patterns/tree/feature3/agent_reflection_framework/agent_reflection_framework)

This ```use case``` demonstrates the process of simulating sequential interactions between AI agents to create, review,
and refine content. It walks through the setup, creation of agents, tasks, and the orchestration of a collaborative
reflection process to improve content quality.

## Features

1. **Conversable Agent Setup**:
   Multiple conversational agents are created using the autogen.AssistantAgent class from the autogen library. These
   agents simulate a collaborative environment where different agents interact and provide feedback on a task.

2. **Writer Agent**:
   The Writer Agent is responsible for generating content based on the given task. In this use case, the task is to
   write a concise and engaging blog post. This agent is set up with the task description and a system message that
   guides it in creating polished content.

    - **Task**: The Writer Agent is tasked with writing a blog post on a specific topic, keeping it concise and
      engaging, while
      adhering to a word limit.

3. **Critic Agent**:
   The Critic Agent reviews the content generated by the Writer Agent. It provides feedback aimed at improving the
   quality of the content, focusing on aspects like clarity, structure, and engagement.

    - **Nested Reviews**: The Critic Agent orchestrates nested feedback from other specialized reviewers (SEO, Legal,
      Ethics,
      etc.), collecting and incorporating their feedback into the refinement process.

4. **Reviewer Agents**:
   Several specialized reviewers provide focused feedback on the content generated by the Writer Agent:

    - **SEO Reviewer**: Reviews the content for search engine optimization (SEO), suggesting improvements to make the
      content more
      discoverable online.
    - **Legal Reviewer**: Ensures the content is legally compliant and free from potential legal issues, providing
      concise
      suggestions for compliance.
    - **Ethics Reviewer**: Assesses the ethical implications of the content, ensuring that it meets ethical standards
      and doesn't
      violate any guidelines.

Each of these reviewers provides feedback in a structured, concise format (within 3 bullet points) and begins their
review by stating their role.

5. **Meta Reviewer Agent**:
   The Meta Reviewer Agent aggregates the feedback from all the specialized reviewers (SEO, Legal, Ethics) and provides
   a final, consolidated review. This agent ensures that all feedback is integrated, and a cohesive final suggestion is
   provided for the Writer Agent to refine the content further.

6. **Reflection and Refinement Process**:
   The core of this framework lies in the reflection process where agents engage in a collaborative review of the Writer
   Agent's work. The Critic Agent initiates nested interactions with the reviewers, gathers their feedback, and
   aggregates it. This feedback loop allows the Writer Agent to refine and enhance the content based on multiple
   perspectives.

    - **Reflection Message**: The Critic Agent sends the content to each reviewer with a reflection message to elicit
      specific
      feedback.

7. **Final Task Execution**:
   After all feedback has been gathered and reviewed, the Writer Agent can refine the content based on the aggregated
   suggestions. The task is completed when the final version of the content is approved, and the feedback loop is
   closed.