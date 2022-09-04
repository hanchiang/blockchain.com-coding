import pytest
from src.service.csv_metadata_parser import CsvMetadataParser

class TestCsvMetadataParser:
    @pytest.mark.asyncio
    async def test_read_file(self):
        data = b"key,value\r\nname,blockchain.com\r\nwebsite,https://www.blockchain.com\r\n"
        expected = {
            "name": "blockchain.com",
            "website": "https://www.blockchain.com"
        }
        csv_metadata_parser = CsvMetadataParser()

        res = await csv_metadata_parser.read_file(data=data)

        assert res == expected



