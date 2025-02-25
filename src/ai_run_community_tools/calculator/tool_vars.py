"""Calculator tools variables."""
from ai_run_community_tools.base.ai_run_tool import ToolMetadata

CALCULATOR_TOOL = ToolMetadata(
    name="calculator_sum",
    label="CalculatorSum",
    description="A simple calculator that adds two integer numbers.",
    user_description="""
    A simple calculator tool that performs basic arithmetic operations.
    Use this tool when you need to add two integer numbers together.
    
    Required inputs:
    - a: First integer number
    - b: Second integer number
    
    Returns the sum of the two numbers.
    """.strip(),
)
