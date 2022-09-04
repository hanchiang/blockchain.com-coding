import pytest
from tests.mock.third_party_order_book_service import ThirdPartyOrderBookServiceImpl


class TestThirdPartyOrderBookService:
    @pytest.mark.asyncio
    async def test_should_cache_trading_pairs_once_without_symbol(self):
        third_party_order_book_service = ThirdPartyOrderBookServiceImpl()
        order_book_list = await third_party_order_book_service.get_order_book()

        assert order_book_list != None

        await third_party_order_book_service.get_order_book()
        assert (
            third_party_order_book_service.get_trading_pairs_and_cache_called_times == 1
        )

    @pytest.mark.asyncio
    async def test_should_cache_trading_pairs_once_with_symbol(self):
        third_party_order_book_service = ThirdPartyOrderBookServiceImpl()
        order_book_list = await third_party_order_book_service.get_order_book(
            symbol="BTC-USD"
        )

        assert order_book_list != None
        assert (
            third_party_order_book_service.get_trading_pairs_and_cache_called_times == 1
        )

        await third_party_order_book_service.get_order_book(symbol="BTC-USDT")
        assert (
            third_party_order_book_service.get_trading_pairs_and_cache_called_times == 1
        )
