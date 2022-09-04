from abc import ABC, abstractmethod
from typing import Any


class MetadataParser(ABC):
    @abstractmethod
    async def read_file(self, data: bytes) -> dict[str, Any]:
        pass
