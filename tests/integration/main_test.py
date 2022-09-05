from typing import Union
import pytest
import asyncio
from typing import Optional
from httpx import AsyncClient
from src.main import app
from src.typings.order_book import OrderBookDto, Bid, Ask

class TestMain:
    def verify_symbol(self, symbol):
        assert len(symbol) > 1
        assert len(symbol.split('-')) == 2

    def verify_bid_ask(self, bids_asks: Union[list[Bid], list[Ask]]):
        fields_to_check = ["price", "quantity", "num_orders"]

        for field_to_check in fields_to_check:
            for bid_ask in bids_asks:
                assert field_to_check in bid_ask

    def verify_order_book(self, order_books: list[OrderBookDto], sort_order: Optional[str] = None):
        prev_symbol = None
        for order_book in order_books:
            symbol = order_book["symbol"]
            self.verify_symbol(symbol)

            if sort_order is not None and prev_symbol is not None:
                if sort_order == "desc":
                    assert prev_symbol > symbol
                else:
                    assert prev_symbol < symbol
                prev_symbol = symbol

            bids = order_book.get("bids", None)
            asks = order_book.get("asks", None)
            
            if bids is not None:
                self.verify_bid_ask(bids)
            if asks is not None:
                self.verify_bid_ask(asks)

    # See: https://pypi.org/project/pytest-asyncio/
    @pytest.fixture(scope="session")
    def event_loop(self):
        policy = asyncio.get_event_loop_policy()
        loop = policy.new_event_loop()
        yield loop
        loop.close()


    @pytest.mark.asyncio
    async def test_get_orderbook_default_sort_descending(self):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            res = await ac.get("/exchanges/blockchain.com/order-books")

            assert res.status_code == 200
            order_books = res.json()["response"]
            assert len(order_books) > 1

            self.verify_order_book(order_books, sort_order="asc")
                

    @pytest.mark.asyncio
    async def test_get_orderbook_sort_descending(self):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            res = await ac.get("/exchanges/blockchain.com/order-books", params={
                "sort_symbol_order": "desc"
            })

            assert res.status_code == 200
            order_books = res.json()["response"]
            assert len(order_books) > 1

            self.verify_order_book(order_books, sort_order="desc")

    @pytest.mark.asyncio
    async def test_get_orderbook_unknown_sort_order_descending(self):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            res = await ac.get("/exchanges/blockchain.com/order-books", params={
                "sort_symbol_order": "unknown"
            })

            assert res.status_code == 200
            order_books = res.json()["response"]
            assert len(order_books) > 1

            self.verify_order_book(order_books, sort_order="desc")
        
    @pytest.mark.asyncio
    async def test_get_orderbook_single_symbol(self):
        loop = asyncio.get_running_loop()
        async with AsyncClient(app=app, base_url="http://test") as ac:
            res = await ac.get("/exchanges/blockchain.com/order-books", params={
                "symbol": "BTC-USD"
            })

            assert res.status_code == 200
            order_books = res.json()["response"]
            assert len(order_books) == 1
            assert order_books[0]["symbol"] == "BTC-USD"

            self.verify_order_book(order_books)



