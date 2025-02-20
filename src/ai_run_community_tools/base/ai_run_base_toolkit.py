"""Base toolkit implementation for AI Run Community Tools."""
from abc import ABC, abstractmethod

from pydantic import BaseModel


class AIRunBaseToolkit(BaseModel, ABC):
    """Base class for AI Run toolkits."""

    @abstractmethod
    def get_tools(self, *args, **kwargs):
        """Get list of tools in the toolkit."""
        pass

    @abstractmethod
    def get_tools_ui_info(self, *args, **kwargs):
        """Get UI information about tools in the toolkit."""
        pass

    @abstractmethod
    def get_toolkit(self, *args, **kwargs):
        """Get toolkit instance."""
        pass