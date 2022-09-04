from typing import TypedDict


class BlockChainBid(TypedDict):
    px: float
    qty: float
    num: float


class BlockChainAsk(TypedDict):
    px: float
    qty: float
    num: float


class BlockChainOrderBookDto(TypedDict):
    symbol: str
    bids: list[BlockChainBid]
    asks: list[BlockChainAsk]
