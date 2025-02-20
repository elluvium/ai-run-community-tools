"""Base tool implementation for AI Run Community Tools."""
import logging
import traceback
from abc import abstractmethod
from typing import Any, Optional

import tiktoken
from langchain_core.tools import BaseTool, ToolException

from ai_run_community_tools.base.errors import TruncatedOutputError
from ai_run_community_tools.base.utils import sanitize_string

logger = logging.getLogger(__name__)


class AIRunBaseTool(BaseTool):
    """Base class for all AIRun community tools."""
    base_name: Optional[str] = None
    handle_tool_error: bool = True
    tokens_size_limit: int = 10000
    throw_truncated_error: bool = True
    truncate_message: str = "Tool output is truncated, make more lightweight query."
    base_llm_model_name: str = "gpt-35-turbo"

    def _run(self, *args, **kwargs):
        try:
            result = self.execute(args, kwargs)
            output, _ = self._limit_output_content(result)
            return output
        except Exception:
            stacktrace = sanitize_string(traceback.format_exc())
            logger.error(f"Error during tool invocation: {self.name}: {stacktrace}")
            raise ToolException(f"Error during {self.name}: {stacktrace}")

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        pass

    def calculate_tokens_count(self, output: Any) -> int:
        encoding = tiktoken.encoding_for_model(self.base_llm_model_name)
        tokens = encoding.encode(str(output))
        return len(tokens)

    def _limit_output_content(self, output: Any) -> Any:
        encoding = tiktoken.encoding_for_model(self.base_llm_model_name)
        tokens = encoding.encode(str(output))
        tokens_count = len(tokens)
        logger.info(f"{self.name}: Tokens size of potential response: {tokens_count}")
        if tokens_count > self.tokens_size_limit:
            truncate_ratio = self.tokens_size_limit / tokens_count
            truncated_data = encoding.decode(tokens[: self.tokens_size_limit])
            truncated = (
                f"{self.truncate_message} Ratio limit/used_tokens: {truncate_ratio}. "
                f"Tool output: {truncated_data}"
            )
            logger.error(
                f"{self.name} output is too long: {tokens_count} tokens. "
                f"Ratio limit/used_tokens: {truncate_ratio} for output tokens {self.tokens_size_limit}"
            )
            if self.throw_truncated_error:
                raise TruncatedOutputError(message=f"{truncated}")
            return truncated, tokens_count
        return output, tokens_count