"""Simple calculator tool implementation."""
from typing import Dict, Any, Type
from pydantic import BaseModel, Field

from ai_run_community_tools.base.ai_run_tool import AIRunTool, ToolMetadata


class CalculatorInput(BaseModel):
    """Input schema for calculator operations."""
    a: int = Field(description="First number for the operation")
    b: int = Field(description="Second number for the operation")


class SimpleCalculatorTool(AIRunTool):
    """A simple calculator tool that performs basic arithmetic operations."""
    
    name: str = "calculator_sum"
    description: str = "A simple calculator that adds two integer numbers."
    args_schema: Type[BaseModel] = CalculatorInput
    metadata: ToolMetadata = ToolMetadata(
        name="calculator_sum",
        label="Calculator Sum",
        description="A simple calculator that adds two integer numbers.",
        user_description="Use this tool when you need to add two integer numbers together."
    )

    def execute(self, a: int, b: int, **kwargs: Dict[str, Any]) -> int:
        """Execute the addition operation.
        
        Args:
            a: First number
            b: Second number
            **kwargs: Additional keyword arguments (not used)
            
        Returns:
            The sum of the two numbers
        """
        return a + b
