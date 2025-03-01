# ai-agentic-design-patterns
AI Agentic Design Patterns with AutoGen


# Usecase 1 : Shark Tank Simulation

This project simulates a Shark Tank-style negotiation between a **Pitcher** (entrepreneur) and a **Panel of Sharks** (investors). It dynamically handles business pitches, investor responses, and deal-making negotiations based on pre-defined evaluation criteria.

## Features

- **Pitcher Introduction**: The pitcher presents their startup, explaining the problem it solves, their sales, revenue, capital table, and the equity shares they are offering.
- **Shark Panel Evaluation**: The sharks ask probing questions and evaluate the pitch based on the pitcher’s projections, valuation, growth potential, and scalability.
- **Negotiations**: Sharks may make counter-offers or close a deal based on factors like:
  - Revenue and scalability of the business.
  - Equity asked vs. business valuation.
  - The pitcher’s conviction and vision for scaling the business.
- **Dynamic Data Input**: The simulation can be run with dynamic data loaded from a JSON file or hardcoded values. Data can be read from an `.env` file to dynamically set the path for the JSON.
- **Multiple Scenarios**: Sharks may make different decisions based on the evaluation, with various negotiation outcomes (offers, counteroffers, or rejection).