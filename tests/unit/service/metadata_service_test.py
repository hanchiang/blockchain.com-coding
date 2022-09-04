import pytest
from asyncio import Future
from typing import Any
from unittest.mock import patch, AsyncMock
from importlib.metadata import metadata
from src.service.metadata_service import MetadataService
from src.dao.metadata_memory_dao import MetadataMemoryDao
from src.service.metadata_parser import MetadataParser

class MetadataParserImpl(MetadataParser):
    async def read_file(self, data: bytes) -> dict[str, Any]:
        return {
            "name": "blockchain.com",
            "website": "https://www.blockchain.com"
        }

class TestMetadataService:
    @pytest.mark.asyncio
    async def test_get_metadata(self):
        metadata_memory_dao = MetadataMemoryDao()
        metadata_memory_dao.metadata = {
            "blockchain.com": {
                "hello": "world"
            }
        }
        expected = {
            "hello": "world"
        }

        metadata_service = MetadataService(metadata_dao=metadata_memory_dao)
        metadata = await metadata_service.get_metadata(exchange_name="blockchain.com")

        assert metadata == expected

    @pytest.mark.asyncio
    async def test_get_metadata_empty(self):
        metadata_memory_dao = MetadataMemoryDao()

        metadata_service = MetadataService(metadata_dao=metadata_memory_dao)
        metadata = await metadata_service.get_metadata(exchange_name="blockchain.com")

        assert metadata == None
        
    async def mock_coroutine(self, x):
        return  {
            "name": "blockchain.com",
            "website": "https://www.blockchain.com"
        }

    @pytest.mark.asyncio
    @patch("src.service.metadata_service.MetadataParserPicker.metadata_parser_picker")
    async def test_upload_metadata(self, metadata_parser_picker_mock):
        metadata_memory_dao = MetadataMemoryDao()
        metadata_service = MetadataService(metadata_dao=metadata_memory_dao)

        metadata_parser_picker_mock.return_value = MetadataParserImpl()
        metadata_memory_dao.save_metadata = AsyncMock(return_value={})

        data = b"key,value\r\nname,blockchain.com\r\nwebsite,https://www.blockchain.com\r\n"
        res = await metadata_service.upload_metadata(exchange_name="blockchain.com", content_type="text/csv", data=data)

        assert res == {}
        metadata_memory_dao.save_metadata.assert_awaited()



        
