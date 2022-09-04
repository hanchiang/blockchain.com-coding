from typing import Any
from src.dao.metadata_dao import MetadataDao
from src.service.metadata_parser_picker import MetadataParserPicker


class MetadataService:
    """Get metadata from storage"""

    def __init__(self, metadata_dao: MetadataDao):
        self.metadata_dao = metadata_dao

    async def get_metadata(self, exchange_name: str) -> dict[str, Any]:
        metadata = await self.metadata_dao.get_metadata(exchange_name=exchange_name)
        return metadata

    async def upload_metadata(self, exchange_name: str, content_type: str, data: bytes):
        metadata_parser = MetadataParserPicker.metadata_parser_picker(
            content_type=content_type
        )
        metadata = await metadata_parser.read_file(data=data)
        res = await self.metadata_dao.save_metadata(exchange_name, data=metadata)
        return res
