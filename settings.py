"""Load LLM settings from .env."""

from __future__ import annotations

import os
from typing import Any

from pydantic import BaseModel, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

_PROVIDER_TO_ENV = {
    "api_key": "AZURE_API_KEY",
    "api_base": "AZURE_API_BASE",
    "api_version": "AZURE_API_VERSION",
}


class LlmConfig(BaseModel):
    model_name: str
    provider_args: dict[str, Any] = {}


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
    )

    llm: LlmConfig

    @model_validator(mode="after")
    def export_litellm_env(self) -> Settings:
        """PageIndex reads Azure creds from env; ADK uses provider_args."""
        for key, env_name in _PROVIDER_TO_ENV.items():
            value = self.llm.provider_args.get(key)
            if value:
                os.environ[env_name] = str(value)
        return self

    @property
    def model_name(self) -> str:
        return self.llm.model_name


def _load_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]


settings = _load_settings()
