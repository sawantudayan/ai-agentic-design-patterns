# Usecase 3: Reflection & Blogpost Writing

This repository demonstrates the creation, configuration, and orchestration of AI agents to generate, review, and refine
a blog post about DeepLearning.AI using a series of Assistant Agents.

## Contents

- Setup
- Agent Creation & Configuration
- Creation & Execution
- Structure for Each Agent
- Contributors

## Setup

To begin, you need to set up the necessary configuration and dependencies:

Dependencies:

- ```autogen```: A library for creating assistant agents.
- OpenAI GPT-3.5 (```gpt-3.5-turbo```): Used as the LLM model to generate text responses.

## Agent Creation & Configuration

In this section, we create and configure various agents that work together to generate, review, and refine content.

### Writer Agent:

- The Writer agent is responsible for generating a concise and engaging blog post about DeepLearning.AI based on the
  provided task.

### Critic Agent:

- The Critic agent reviews the generated content and provides constructive feedback to improve its quality.

## Creation & Execution

Now that we have our agents configured, we will define a task and initiate the creation process.

### Task Definition:

- We define a task where the Writer needs to create a concise blog post about DeepLearning.AI within 150 words.

### Initiating the Writer Agent:

- We send the task to the Writer agent to generate the blog post.

## Structure for Each Agent

Each agent has a distinct structure and role:

### Writer Agent:

- Role: Generates a blog post based on the task.
- Configuration: Uses the system_message to guide content creation, ensuring that only the final version of the blog
  post is returned without additional comments.

### Critic Agent:

- Role: Reviews the generated content and provides constructive feedback.
- Configuration: Uses the system_message to guide its review process.

### Reviewers:

Several specialized reviewers will examine the content:

- SEO Reviewer: Optimizes the content for search engines.
- Legal Reviewer: Ensures the content is legally compliant.
- Ethics Reviewer: Checks for ethical concerns.
- Meta Reviewer: Aggregates feedback from all reviewers to give final suggestions.

### Contributors

This task involves a collaborative effort between various agents to generate, review, and refine content:

- Writer Agent: Responsible for creating the initial blog post.
- Critic Agent: Provides feedback to improve the quality of the content.
- SEO Reviewer: Reviews content for search engine optimization.
- Legal Reviewer: Ensures the content adheres to legal standards.
- Ethics Reviewer: Reviews the content for ethical concerns.
- Meta Reviewer: Aggregates feedback from all reviewers and provides a final recommendation.


