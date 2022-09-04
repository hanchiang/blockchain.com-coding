from typing import TypedDict


class Bid(TypedDict):
    price: float
    quantity: float
    num_orders: float


class Ask(TypedDict):
    price: float
    quantity: float
    num_orders: float


class OrderBookDto(TypedDict):
    symbol: str
    bids: list[Bid]
    asks: list[Ask]
