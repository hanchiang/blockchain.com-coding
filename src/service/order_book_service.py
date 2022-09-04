from typing import Optional
from .third_party_order_book_service import ThirdPartyOrderBookService
from src.typings.order_book import OrderBookDto
from src.transformer.third_party_order_book_transformer import (
    ThirdPartyOrderBookTransformer,
)


class OrderBookService:
    """Get order book details from exchange"""

    def __init__(
        self,
        third_party_order_book_service: ThirdPartyOrderBookService,
        third_party_order_book_transformer: ThirdPartyOrderBookTransformer,
    ):
        self.third_party_order_book_service = third_party_order_book_service
        self.third_party_order_book_transformer = third_party_order_book_transformer

    async def get_order_book(
        self,
        symbol: Optional[str],
        order_type: Optional[str],
        sort_symbol_order: Optional[str],
    ) -> list[OrderBookDto]:
        order_book_list = await self.third_party_order_book_service.get_order_book(
            symbol=symbol
        )
        return self.third_party_order_book_transformer.tranform_to_standard_order_book(
            order_book_list,
            symbol=symbol,
            order_type=order_type,
            sort_symbol_order=sort_symbol_order,
        )
