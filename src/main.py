from typing import Optional
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

from service.order_book_service import OrderBookService
from dependencies.dependencies import Dependencies

Dependencies.build()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/exchanges/{exchange_name}/order-books")
async def get_orderbook(
    exchange_name: str,
    symbol: Optional[str] = None,
    order_type: Optional[str] = None,
    sort_symbol_order: Optional[str] = None,
):
    blockchain_order_service = Dependencies.get_order_book_service(exchange_name)
    blockchain_transformer_service = Dependencies.get_order_book_transformer(
        exchange_name
    )

    order_book_service = OrderBookService(
        third_party_order_book_service=blockchain_order_service,
        third_party_order_book_transformer=blockchain_transformer_service,
    )
    res = await order_book_service.get_order_book(
        symbol=symbol, order_type=order_type, sort_symbol_order=sort_symbol_order
    )
    return {"response": res}


@app.get("/exchange/{exchange_name}/metadata")
async def get_metadata():
    pass
