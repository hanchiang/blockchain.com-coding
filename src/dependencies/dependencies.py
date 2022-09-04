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
from typing import Any


class Dependencies:
    order_book_service: dict[str, ThirdPartyOrderBookService] = {}
    order_book_transformer: dict[str, ThirdPartyOrderBookTransformer] = {}

    @staticmethod
    def build():
        Dependencies.order_book_service = {
            "blockchain.com": BlockChainOrderBookService(
                base_url=Config.get_env_var("BLOCKCHAIN_BASE_URL")
            )
        }

        Dependencies.order_book_transformer = {
            "blockchain.com": BlockChainOrderBookTransformer()
        }

    @staticmethod
    def get_order_book_service(key: str) -> ThirdPartyOrderBookService:
        service = Dependencies.order_book_service.get(key, None)
        if service is None:
            raise DependencyNotFoundException(
                f"Unable to find order book service for {key}"
            )
        return service

    @staticmethod
    def get_order_book_transformer(key: str) -> ThirdPartyOrderBookTransformer:
        transformer = Dependencies.order_book_transformer.get(key, None)
        if transformer is None:
            raise DependencyNotFoundException(
                f"Unable to find order book transformer for {key}"
            )
        return transformer
