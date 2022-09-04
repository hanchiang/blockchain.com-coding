from typing import Optional, Any
from abc import ABC, abstractmethod
from src.http_client.http_client import HttpClient


class ThirdPartyOrderBookService(ABC):
    def __init__(self, base_url: str):
        self.client = HttpClient(base_url=base_url)
        self.trading_pairs: dict[str, Any] = {}

    def is_trading_pairs_cached(self, symbol: Optional[str] = None) -> bool:
        return (symbol is not None and symbol in self.trading_pairs) or (
            len(self.trading_pairs) > 0
        )

    @abstractmethod
    async def get_trading_pairs_and_cache(self) -> None:
        """Get a list of trading pairs from exchange and cache it"""
        pass

    async def get_order_book(self, symbol: Optional[str] = None) -> list[Any]:
        """Returns the quantity and average price of the order book(asks and bids) for each symbol"""
        if not self.is_trading_pairs_cached(symbol=symbol):
            await self.get_trading_pairs_and_cache()
        res = await self.get_order_book_from_exchange(symbol=symbol)
        return res

    @abstractmethod
    async def get_order_book_from_exchange(self, symbol: Optional[str]) -> list[Any]:
        pass
