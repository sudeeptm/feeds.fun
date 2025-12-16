import pydantic_settings

from ffun.core.settings import BaseSettings


class Settings(BaseSettings):
    api_entry_point: str | None = "http://localhost:11434/v1"
    api_timeout: float = 60.0

    model_config = pydantic_settings.SettingsConfigDict(env_prefix="FFUN_LOCAL_LLM_")


settings = Settings()
