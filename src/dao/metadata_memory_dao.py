from .metadata_dao import MetadataDao
from typing import Any


class MetadataMemoryDao(MetadataDao):
    def __init__(self):
        self.metadata = {}

    async def get_metadata(self, exchange_name: str):
        return self.metadata.get(exchange_name, None)

    async def save_metadata(self, exchange_name: str, data: dict[str, Any]):
        self.metadata[exchange_name] = data
