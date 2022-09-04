from src.service.order_book_service import OrderBookService
from tests.mock.third_party_order_book_service import ThirdPartyOrderBookServiceImpl


class TestOrderBookService:
    def test_process_order_book(self):
        third_party_order_book_service = ThirdPartyOrderBookServiceImpl()
