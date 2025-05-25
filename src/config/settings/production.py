from fastapi.src.config.settings.base import BackendBaseSettings
from fastapi.src.config.settings.environment import Environment


class BackendProdSettings(BackendBaseSettings):
    DESCRIPTION: str | None = "Production Environment"
    ENVIRONMENT: Environment = Environment.PRODUCTION
