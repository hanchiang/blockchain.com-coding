import pytest
from src.service.metadata_parser_picker import MetadataParserPicker
from src.service.csv_metadata_parser import CsvMetadataParser
from src.exceptions.exceptions import UnknownFileTypeException

class TestMetadataParserPicker:
    def test_csv_metadata_parser(self):
        metadata_parser = MetadataParserPicker.metadata_parser_picker(content_type="text/csv")
        assert isinstance(metadata_parser, CsvMetadataParser)

    def test_unknown_metadata_parser(self):
        with pytest.raises(UnknownFileTypeException):
            MetadataParserPicker.metadata_parser_picker(content_type="random")