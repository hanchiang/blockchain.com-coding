from typing import Any, Optional
from src.service.third_party_order_book_service import ThirdPartyOrderBookService


class ThirdPartyOrderBookServiceImpl(ThirdPartyOrderBookService):
    def __init__(self):
        self.trading_pairs: dict[str, Any] = {}
        self.get_trading_pairs_and_cache_called_times = 0

    async def get_trading_pairs_and_cache(self):
        self.trading_pairs = {"BTC-USD": "BTC-USD", "BTC-USDT": "BTC-USDT"}
        self.get_trading_pairs_and_cache_called_times += 1

    async def get_order_book_from_exchange(self, symbol: Optional[str]) -> list[Any]:
        order_book = {
            "symbol": symbol,
            "bids": [
                {"px": 20000, "qty": 0.1, "num": 1000},
                {"px": 19999, "qty": 0.2, "num": 2000},
            ],
            "asks": [
                {"px": 20005, "qty": 0.1, "num": 1000},
                {"px": 20003, "qty": 0.2, "num": 2000},
            ],
        }
        return [order_book]
