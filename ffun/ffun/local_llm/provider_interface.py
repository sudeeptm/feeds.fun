from ffun.local_llm.settings import settings
from ffun.llms_framework.entities import LLMProvider
from ffun.openai.provider_interface import OpenAIInterface


class LocalLLMInterface(OpenAIInterface):
    provider = LLMProvider.local

    def __init__(self) -> None:
        super().__init__(api_entry_point=settings.api_entry_point, api_timeout=settings.api_timeout)


provider = LocalLLMInterface()
