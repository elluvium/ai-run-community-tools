"""Models for AI Run Community Tools."""
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class ToolSet(str, Enum):
    """Available tool sets."""
    CALCULATOR = "calculator"
    CALCULATOR_LABEL = "Calculator"


class Tool(BaseModel):
    """Tool metadata model."""
    name: str
    label: str
    description: str
    settings_config: bool = False


class ToolKit(BaseModel):
    """Toolkit metadata model."""
    toolkit: ToolSet
    tools: List[Tool]
    settings_config: bool = False
    label: Optional[str] = None