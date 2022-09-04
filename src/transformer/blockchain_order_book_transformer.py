from typing import Any, Optional, cast
from src.typings.order_book import OrderBookDto
from .third_party_order_book_transformer import ThirdPartyOrderBookTransformer


class BlockChainOrderBookTransformer(ThirdPartyOrderBookTransformer):
    def tranform_to_standard_order_book(
        self,
        order_book_list: list[Any],
        symbol: Optional[str],
        order_type: Optional[str],
        sort_symbol_order: Optional[str],
    ) -> list[OrderBookDto]:
        return self.transform_order_book(
            order_book_list=order_book_list,
            symbol=symbol,
            order_type=order_type,
            sort_symbol_order=sort_symbol_order,
        )

    def transform_order_book(
        self,
        order_book_list: list[Any],
        symbol: Optional[str] = None,
        order_type: Optional[str] = None,
        sort_symbol_order: Optional[str] = None,
    ) -> list[OrderBookDto]:
        order_books_list = self.filter_order_book(
            order_books_list=order_book_list, order_type=order_type
        )
        return self.process_order_book(
            order_books_list, sort_symbol_order=sort_symbol_order
        )

    def filter_order_book(
        self, order_books_list: list[OrderBookDto], order_type: Optional[str] = None
    ):
        res = []

        for order_book in order_books_list:
            sym = order_book["symbol"]
            bids = order_book["bids"]
            asks = order_book["asks"]

            if order_type is not None:
                if order_type.lower() == "bid":
                    res.append({"symbol": sym, "bids": bids})
                elif order_type.lower() == "ask":
                    res.append({"symbol": sym, "asks": asks})
            else:
                res.append(order_book)

        return res

    def process_order_book(
        self,
        order_books_list: list[Any],
        sort_symbol_order: Optional[str] = None,
    ) -> list[OrderBookDto]:
        if sort_symbol_order is not None:
            is_reverse_order = True if sort_symbol_order.lower() == "desc" else False
            order_books_list.sort(key=lambda o: o["symbol"], reverse=is_reverse_order)

        return list(map(self.map_to_order_book, order_books_list))

    def map_to_order_book(self, order_book: Any) -> OrderBookDto:
        symbol = order_book["symbol"]
        asks = order_book.get("asks", [])
        bids = order_book.get("bids", [])

        transformed_order_book = {}
        key_name_map = {"px": "price", "qty": "quantity", "num": "num_orders"}
        transformed_order_book["symbol"] = symbol

        if len(bids) > 0:
            transformed_order_book["bids"] = self.map_bid_ask(
                bids_asks=bids, key_map=key_name_map
            )
        if len(asks) > 0:
            transformed_order_book["asks"] = self.map_bid_ask(
                bids_asks=asks, key_map=key_name_map
            )

        return cast(OrderBookDto, transformed_order_book)

    def map_bid_ask(self, bids_asks: list[Any], key_map: dict[str, str]):
        res = []
        for bid_ask in bids_asks:
            transformed_bid_ask = {}
            for k, v in bid_ask.items():
                transformed_bid_ask[key_map[k]] = v
            res.append(transformed_bid_ask)
        return res
