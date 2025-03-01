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

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Code Overview](#code-overview)
5. [Contributors](#contributors)

## Installation

To use the Shark Tank Simulation, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/yourusername/shark-tank-simulation.git
cd shark-tank-simulation
```


2. Install required packages:

```bash
pip install -r requirements.txt
```

  You may need to install the python-dotenv package to read environment variables:

  ```bash
  pip install python-dotenv
  ```





## Usage
You can run the Shark Tank Simulation in two different ways:

1. Jupyter Notebook Implementation
 - Open shark_tank_simulator.ipynb in Jupyter Notebook or JupyterLab.
 - The notebook will walk you through each part of the simulation process step by step, from setting up the pitcher and sharks to running the simulation.
2. Python Class-Based Implementation
 - Ensure you have the necessary environment variables set up, especially the path to the shark_tank_data.json file in the .env file.
 - Run shark_tank_simulator.py to execute the simulation with the default setup or modify the JSON file as needed for custom simulations.
```bash
python shark_tank_simulator.py
```


## Features

### Pitcher:
 - Business Overview: Introduces the startup's mission, sales, and growth.
 - Revenue: Pitcher provides annual revenue and growth rate projections.
 - Valuation: The equity offer is compared to the startup’s valuation.
 - Equity Asked: The pitcher asks for a specific percentage of equity for a certain investment amount.
 - Scalability: The pitcher discusses the scalability of the business, including plans for growth and expansion.

### Sharks:
 - Shark Panel: There are multiple sharks who evaluate the pitch based on specific criteria.
 - Conviction Factor: Each shark has a conviction factor, which is a parameter that influences how likely they are to invest based on their perception of the pitcher's vision and business.
 - Investment Decision: Sharks decide whether to make an offer, negotiate terms, or reject the deal based on factors like:
    - Pitcher's revenue and growth projections.
    - Business scalability.
    - Equity vs valuation.
    - Conviction in the pitcher's vision.
  

### Negotiations:
 - Sharks may make counter-offers or close deals based on their evaluations.
 - The conversation flow is dynamic, with sharks negotiating equity offers and pitcher responses.
 - The decision logic is implemented to simulate real-world Shark Tank scenarios.


### Environment Variables:
 - The project reads from a .env file to get the path to the JSON file containing the simulation data. The .env file contains the following:

```env
SHARK_TANK_JSON_PATH="path/to/shark_tank_data.json"
```

### Dynamic Data from JSON:
 - The data for the pitcher and sharks is loaded from a shark_tank_data.json file. This allows the simulation to be flexible and run with different pitches or investor panels.


## Code Overview

### SharkTankSimulation Class:
 - Simulates the overall Shark Tank event, including the interaction between the pitcher and the sharks.
`- Handles logic for deal-making, counter-offers, and negotiations.

### Pitcher Class:
 - Represents the entrepreneur who presents the pitch.
 - Contains attributes such as business revenue, valuation, and equity asked.

### Shark Class:
 - Represents the investors who evaluate the pitch.
 - Each shark has a conviction factor and evaluates the pitch based on predefined rules.

### Evaluation Criteria:
 - Revenue: Sharks are more likely to invest if the pitcher demonstrates strong financials.
 - Scalability: The business must be scalable for sharks to invest.
 - Conviction: A high level of conviction from the pitcher can increase the chances of a deal.
 - Unreasonable Valuation: If the pitcher asks for an unrealistic valuation, sharks may counter with a lower offer.

## Dynamic Interaction:
 - The simulation allows for multiple rounds of negotiation and questions between the pitcher and sharks.
 - Shark offers can vary based on pitch quality, revenue, scalability, and more.


## Contributors
Udayan Sawant - Creator and Developer
