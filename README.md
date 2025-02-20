# AI Run Community Tools

This package provides additional tools for the Codemie platform, implemented by the AI Run community.

## Features

Currently includes:
- Calculator toolkit with sum calculator tool

## Installation

```bash
pip install ai-run-community-tools
```

## Usage

```python
from ai_run_community_tools.calculator import CalculatorToolkit

# Initialize the toolkit
calculator_toolkit = CalculatorToolkit.get_toolkit()

# Get available tools
tools = calculator_toolkit.get_tools()

# Use sum calculator
sum_tool = tools[0]
result = sum_tool.invoke({"num1": 5, "num2": 3})  # Returns 8
```