import csv
import io
from typing import Any
from .metadata_parser import MetadataParser


class CsvMetadataParser(MetadataParser):
    def __init__(self):
        super().__init__()

    async def read_file(self, data: bytes) -> dict[str, Any]:
        decoded = data.decode("utf-8")
        metadata = {}
        reader = csv.DictReader(io.StringIO(decoded))

        for row in reader:
            key = row.get("key", None) or row.get("Key", None)
            value = row.get("value", None) or row.get("Value", None)
            if key is not None and value is not None:
                metadata[key.lower()] = value
        return metadata
