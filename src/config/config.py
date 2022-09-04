import os
from typing import Any
from src.exceptions.exceptions import EnvironmentVariableNotFoundException


class Config:
    env_var: dict[str, Any]

    @staticmethod
    def get_env_var(env: str) -> str:
        res = os.getenv(env, None)
        if res is None:
            raise EnvironmentVariableNotFoundException(
                f"Environment variable {env} is not found"
            )
        return res

    @staticmethod
    def get_env_vars_in_app() -> dict[str, str]:
        return {"blockchain_base_url": Config.get_env_var("BLOCKCHAIN_BASE_URL")}
