"""Base tool implementation for AI tools."""
import logging
import traceback
from abc import abstractmethod
from typing import Any, Dict, Optional, Type

from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.tools import BaseTool, ToolException
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class ToolMetadata(BaseModel):
    """Metadata for AI tools."""
    name: str
    label: str
    description: str
    user_description: Optional[str] = None


class AIRunTool(BaseTool):
    """Base class for AI tools implementation.
    
    This class combines the best practices from both Alita and Codemie tools
    to provide a robust base for AI tool implementation.
    """
    name: str = ""
    description: str = ""
    metadata: Optional[ToolMetadata] = None
    args_schema: Optional[Type[BaseModel]] = None
    #api_wrapper: Optional[BaseModel] = Field(default_factory=BaseModel)
    handle_tool_error: Optional[bool] = True

    def _run(
        self,
        *args: Any,
        run_manager: Optional[CallbackManagerForToolRun] = None,
        **kwargs: Dict[str, Any],
    ) -> str | Dict[str, Any]:
        """Execute the tool operation.

        Args:
            *args: Positional arguments to pass to the tool
            run_manager: Optional callback manager for tool runs
            **kwargs: Keyword arguments to pass to the tool

        Returns:
            Tool execution result as string or dict

        Raises:
            ToolException: If an error occurs during tool execution
        """
        try:
            logger.debug(f"Executing {self.name} with args: {args}, kwargs: {kwargs}")
            result = self.execute(*args, **kwargs) 
            return result
        except Exception as e:
            error_msg = f"Error during {self.name} execution: {str(e)}\n{traceback.format_exc()}"
            logger.error(error_msg)
            if self.handle_tool_error:
                return f"Tool execution failed: {str(e)}"
            raise ToolException(error_msg)

    @abstractmethod
    def execute(self, *args: Any, **kwargs: Dict[str, Any]) -> Any:
        """Execute the core tool logic.
        
        This method must be implemented by concrete tool classes.

        Args:
            *args: Positional arguments for the tool execution
            **kwargs: Keyword arguments for the tool execution

        Returns:
            Tool execution result
        """
        pass
