import json
from config import MODEL_COSTS

def calculate_cost(usage, model):
    # Implement cost calculation logic here
    pass

def update_cumulative_costs(additional_input_cost, additional_output_cost):
    """Update cumulative costs based on the latest API call."""
    try:
        with open('cumulative_costs.json', 'r+') as file:
            costs = json.load(file)
            costs['cumulative_input_cost'] += additional_input_cost
            costs['cumulative_output_cost'] += additional_output_cost
            costs['cumulative_total_cost'] += additional_input_cost + additional_output_cost

            file.seek(0)
            json.dump(costs, file, indent=4)
            file.truncate()
    except FileNotFoundError:
        # Initialize the file if it does not exist
        with open('cumulative_costs.json', 'w') as file:
            json.dump({
                "cumulative_input_cost": additional_input_cost,
                "cumulative_output_cost": additional_output_cost,
                "cumulative_total_cost": additional_input_cost + additional_output_cost
            }, file, indent=4)

def read_cumulative_costs():
    """Read and return cumulative costs."""
    try:
        with open('cumulative_costs.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # Return zeros if the file does not exist
        return {
            "cumulative_input_cost": 0.0,
            "cumulative_output_cost": 0.0,
            "cumulative_total_cost": 0.0
        }
