from typing import Any
from src.config.config import Config
from src.service.blockchain_order_book_service import BlockChainOrderBookService
from src.service.third_party_order_book_service import ThirdPartyOrderBookService
from src.transformer.blockchain_order_book_transformer import (
    BlockChainOrderBookTransformer,
)
from src.transformer.third_party_order_book_transformer import (
    ThirdPartyOrderBookTransformer,
)
from src.exceptions.exceptions import DependencyNotFoundException
from src.dao.metadata_dao import MetadataDao
from src.dao.metadata_memory_dao import MetadataMemoryDao
from src.service.metadata_parser import MetadataParser
from src.service.csv_metadata_parser import CsvMetadataParser


class Dependencies:
    order_book_service: dict[str, ThirdPartyOrderBookService] = {}
    order_book_transformer: dict[str, ThirdPartyOrderBookTransformer] = {}
    metadata_dao: dict[str, MetadataDao] = {}
    metadata_parser: dict[str, MetadataParser] = {}
    is_initialised = False

    @staticmethod
    def build():
        if not Dependencies.is_initialised:
            Dependencies.build_order_book_service()
            Dependencies.build_order_book_transformer()
            Dependencies.build_order_book_metadata_dao()
            Dependencies.build_order_book_metadata_parser()
            Dependencies.is_initialised = True

    @staticmethod
    def build_order_book_service():
        Dependencies.order_book_service = {
            "blockchain.com": BlockChainOrderBookService(
                base_url=Config.get_env_var("BLOCKCHAIN_BASE_URL")
            )
        }

    @staticmethod
    def build_order_book_transformer():
        Dependencies.order_book_transformer = {
            "blockchain.com": BlockChainOrderBookTransformer()
        }

    @staticmethod
    def build_order_book_metadata_dao():
        Dependencies.metadata_dao = {"memory": MetadataMemoryDao()}

    @staticmethod
    def build_order_book_metadata_parser():
        Dependencies.metadata_parser = {"csv": CsvMetadataParser()}

    @staticmethod
    def get_order_book_service(key: str) -> ThirdPartyOrderBookService:
        Dependencies.build()
        service = Dependencies.order_book_service.get(key, None)
        if service is None:
            raise DependencyNotFoundException(
                f"Unable to find order book service for {key}"
            )
        return service

    @staticmethod
    def get_order_book_transformer(key: str) -> ThirdPartyOrderBookTransformer:
        Dependencies.build()
        transformer = Dependencies.order_book_transformer.get(key, None)
        if transformer is None:
            raise DependencyNotFoundException(
                f"Unable to find order book transformer for {key}"
            )
        return transformer

    @staticmethod
    def get_metadata_dao(key: str) -> MetadataDao:
        Dependencies.build()
        res = Dependencies.metadata_dao.get(key, None)
        if res is None:
            raise DependencyNotFoundException(f"Unable to find metadata dao for {key}")
        return res

    @staticmethod
    def get_metadata_parser(key: str) -> MetadataParser:
        Dependencies.build()
        res = Dependencies.metadata_parser.get(key, None)
        if res is None:
            raise DependencyNotFoundException(
                f"Unable to find metadata reader for {key}"
            )
        return res
