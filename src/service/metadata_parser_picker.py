from src.dependencies.dependencies import Dependencies
from src.service.metadata_parser import MetadataParser
from src.exceptions.exceptions import UnknownFileTypeException


class MetadataParserPicker:
    @staticmethod
    def metadata_parser_picker(content_type) -> MetadataParser:
        if content_type == "text/csv":
            return Dependencies.get_metadata_parser("csv")
        else:
            raise UnknownFileTypeException(f"Unable to open file type {content_type}")
