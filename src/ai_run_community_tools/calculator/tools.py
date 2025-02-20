"""Calculator tools implementation."""
from typing import Any

from ai_run_community_tools.base import AIRunBaseTool
from pydantic import BaseModel, Field


class SumCalculatorInput(BaseModel):
    """Input for sum calculator tool."""
    num1: float = Field(..., description="First number to add")
    num2: float = Field(..., description="Second number to add")


class SumCalculatorTool(AIRunBaseTool):
    """Tool to calculate sum of two numbers."""
    name = "sum_calculator"
    description = "Tool to calculate sum of two numbers"
    args_schema = SumCalculatorInput

    def execute(self, *args: Any, **kwargs: Any) -> float:
        """Calculate sum of two numbers."""
        # Extract numbers from kwargs which come from args_schema
        num1 = kwargs.get('num1', 0)
        num2 = kwargs.get('num2', 0)
        
        return num1 + num2