import decouple

from functools import lru_cache
from fastapi.src.config.settings.base import BackendBaseSettings
from fastapi.src.config.settings.development import BackendDevSettings
from fastapi.src.config.settings.environment import Environment
from fastapi.src.config.settings.production import BackendProdSettings
from fastapi.src.config.settings.staging import BackendStageSettings


class BackendSettingsFactory:
    def __init__(self, environment: str):
        self.environment = environment

    def __call__(self) -> BackendBaseSettings:
        if self.environment == Environment.DEVELOPMENT.value:
            return BackendDevSettings()
        elif self.environment == Environment.STAGING.value:
            return BackendStageSettings()
        return BackendProdSettings()


@lru_cache()
def get_settings() -> BackendBaseSettings:
    return BackendSettingsFactory(environment=decouple.config("ENVIRONMENT", default="DEV", cast=str))()


settings: BackendBaseSettings = get_settings()
