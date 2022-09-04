from typing import Any, Optional
from abc import ABC, abstractmethod
from src.typings.order_book import OrderBookDto


class ThirdPartyOrderBookTransformer(ABC):
    @abstractmethod
    def tranform_to_standard_order_book(
        self,
        order_books: list[Any],
        symbol: Optional[str],
        order_type: Optional[str],
        sort_symbol_order: Optional[str],
    ) -> list[OrderBookDto]:
        return []
