"""Tool metadata for calculator tools."""
from ai_run_community_tools.base.models import Tool

CALCULATOR_TOOL = Tool(
    name="sum_calculator",
    label="Sum Calculator",
    description="Tool to calculate sum of two numbers",
    settings_config=False,
)