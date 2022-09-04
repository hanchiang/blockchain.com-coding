import pytest
from asyncio import Future
from unittest.mock import AsyncMock, Mock, patch
from src.service.blockchain_order_book_service import BlockChainOrderBookService


class TestBlockChainOrderBookService:
    async def orderbook_coroutine(self, x):
        return {}

    @pytest.fixture
    def orderbook(self):
        return {"symbol": "BTC-USD"}

    @pytest.fixture
    def trading_pairs(self):
        return {"BTC-USD": "BTC-USD", "BTC-USDT": "BTC-USDT"}

    @pytest.mark.asyncio
    async def test_get_order_book_from_exchange_without_symbol(
        self, orderbook, trading_pairs
    ):
        blockchain_order_service = BlockChainOrderBookService(base_url="domain")
        blockchain_order_service.trading_pairs = trading_pairs
        blockchain_order_service.get_l3_order_book = AsyncMock(return_value=[orderbook])

        order_book_list = await blockchain_order_service.get_order_book_from_exchange()

        assert order_book_list == [orderbook]

        blockchain_order_service.get_l3_order_book.assert_awaited_with(
            list(blockchain_order_service.trading_pairs.keys())
        )

    @pytest.mark.asyncio
    async def test_get_order_book_from_exchange_with_symbol(
        self, orderbook, trading_pairs
    ):
        blockchain_order_service = BlockChainOrderBookService(base_url="domain")
        blockchain_order_service.trading_pairs = trading_pairs
        blockchain_order_service.get_l3_order_book = AsyncMock(return_value=[orderbook])

        order_book_list = await blockchain_order_service.get_order_book_from_exchange(
            symbol="BTC-USD"
        )

        assert order_book_list == [orderbook]

        blockchain_order_service.get_l3_order_book.assert_awaited_with(["BTC-USD"])

    @pytest.mark.asyncio
    async def test_get_trading_pairs_and_cache(self, trading_pairs):
        blockchain_order_service = BlockChainOrderBookService(base_url="domain")
        blockchain_order_service.get_trading_pairs = AsyncMock(
            return_value=trading_pairs
        )

        await blockchain_order_service.get_trading_pairs_and_cache()

        assert blockchain_order_service.trading_pairs == trading_pairs

    @pytest.mark.asyncio
    @patch("asyncio.gather", new_callable=AsyncMock)
    async def test_get_l3_order_book(self, asyncio_gather_mock):
        blockchain_order_service = BlockChainOrderBookService(base_url="domain")
        blockchain_order_service.client = Mock(
            return_value={"get": self.orderbook_coroutine}
        )

        await blockchain_order_service.get_l3_order_book(["BTC-USD"])

        asyncio_gather_mock.return_value = Future()
        asyncio_gather_mock.assert_awaited()
