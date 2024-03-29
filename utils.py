from config import MODEL_COSTS
from cost_manager import update_cumulative_costs, read_cumulative_costs

from rich.console import Console
from rich.text import Text
from rich import box
from rich.panel import Panel
from rich.table import Table

console = Console()

def print_token_info(usage, model='gpt-3.5-turbo-0125'):
    model_costs = MODEL_COSTS.get(model, {})
    input_cost = model_costs.get("input_cost_per_million_tokens", 0)
    output_cost = model_costs.get("output_cost_per_million_tokens", 0)

    # Calculate the cost for the used tokens
    prompt_cost = usage['prompt_tokens'] / 1_000_000 * input_cost
    completion_cost = usage['completion_tokens'] / 1_000_000 * output_cost
    total_cost = prompt_cost + completion_cost

    # Update cumulative costs
    update_cumulative_costs(prompt_cost, completion_cost)

    # Read and print cumulative costs
    cumulative_costs = read_cumulative_costs()

    table = Table(title="LLM Usage and Costs", box=box.DOUBLE)
    table.add_column("Type", style="cyan", no_wrap=True)
    table.add_column("Tokens", style="magenta")
    table.add_column("Cost (USD)", style="green")
    table.add_column("Cumulative Cost (USD)", style="yellow")

    table.add_row("Input (Prompt)", str(usage['prompt_tokens']), f"${prompt_cost:.6f}", f"${cumulative_costs['cumulative_input_cost']:.6f}")
    table.add_row("Output (Response)", str(usage['completion_tokens']), f"${completion_cost:.6f}", f"${cumulative_costs['cumulative_output_cost']:.6f}")
    table.add_row("Total", str(usage['total_tokens']), f"${total_cost:.6f}", f"${cumulative_costs['cumulative_total_cost']:.6f}")
    
    console.print(table)
