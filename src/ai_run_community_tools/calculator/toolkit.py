"""Calculator toolkit implementation."""
from typing import List

from langchain_core.tools import BaseTool

from ai_run_community_tools.base import AIRunBaseToolkit
from ai_run_community_tools.calculator.tools import SumCalculatorTool
from ai_run_community_tools.calculator.tools_vars import CALCULATOR_TOOL
from ai_run_community_tools.base.models import ToolKit, ToolSet


class CalculatorToolkitUI(ToolKit):
    """Calculator toolkit UI representation."""
    toolkit: ToolSet = ToolSet.CALCULATOR
    tools: List[Tool] = [
        CALCULATOR_TOOL,
    ]


class CalculatorToolkit(AIRunBaseToolkit):
    """Calculator toolkit implementation."""

    @classmethod
    def get_tools_ui_info(cls, *args, **kwargs):
        """Get UI information about calculator tools."""
        return CalculatorToolkitUI().model_dump()

    def get_tools(self) -> List[BaseTool]:
        """Get list of calculator tools."""
        tools = [
            SumCalculatorTool(),
        ]
        return tools

    @classmethod
    def get_toolkit(cls, configs: dict = None):
        """Get calculator toolkit instance."""
        return cls()