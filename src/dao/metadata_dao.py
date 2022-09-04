from abc import ABC, abstractmethod
from typing import Any


class MetadataDao(ABC):
    @abstractmethod
    async def get_metadata(self, exchange_name: str) -> dict[str, Any]:
        """Gets all key value pairs"""
        pass

    @abstractmethod
    async def save_metadata(self, exchange_name: str, data: dict[str, Any]):
        """"""
        pass
