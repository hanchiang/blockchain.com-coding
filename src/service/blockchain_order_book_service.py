import asyncio
from typing import Any, Optional
from .third_party_order_book_service import ThirdPartyOrderBookService
from src.typings.order_book import OrderBookDto


class BlockChainOrderBookService(ThirdPartyOrderBookService):
    def __init__(self, base_url: str):
        super().__init__(base_url=base_url)
        self.trading_pairs: dict[str, Any] = {}

    async def get_trading_pairs_and_cache(self):
        trading_pair_res = await self.get_trading_pairs()
        print(f"There are {len(trading_pair_res.keys())} trading pairs")
        for key in trading_pair_res.keys():
            self.trading_pairs[key] = key

    async def get_order_book_from_exchange(
        self, symbol: Optional[str] = None
    ) -> list[Any]:
        trading_pairs: list[str] = (
            [symbol] if symbol is not None else list(self.trading_pairs.keys())
        )
        order_books_list = await self.get_l3_order_book(trading_pairs)
        return order_books_list

    async def get_trading_pairs(self):
        """Return all trading pairs that are supported"""
        res = await self.client.get("/symbols")
        return res

    async def get_l3_order_book(self, trading_pairs: list[str]) -> list[OrderBookDto]:
        """Return L3 order book for a symbol"""
        tasks = []
        for trading_pair in trading_pairs:
            tasks.append(self.client.get(f"/l3/{trading_pair}"))

        res = await asyncio.gather(*tasks)
        return res
