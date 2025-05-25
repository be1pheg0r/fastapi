from fastapi.src.config.settings.base import BackendBaseSettings
from fastapi.src.config.settings.environment import Environment


class BackendStageSettings(BackendBaseSettings):
    DESCRIPTION: str | None = "Test Environment"
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.STAGING
