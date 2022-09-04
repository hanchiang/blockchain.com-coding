from typing import Optional
from fastapi import FastAPI, UploadFile
from dotenv import load_dotenv
from dependencies.dependencies import Dependencies
from service.order_book_service import OrderBookService
from service.metadata_service import MetadataService

load_dotenv()

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
async def get_metadata(exchange_name: str):
    metadata_dao = Dependencies.get_metadata_dao("memory")
    metadata_service = MetadataService(metadata_dao=metadata_dao)

    res = await metadata_service.get_metadata(exchange_name=exchange_name)

    return {"response": res}


@app.put("/exchange/{exchange_name}/metadata")
async def upload_metadata(exchange_name: str, file: UploadFile):
    metadata_dao = Dependencies.get_metadata_dao("memory")

    data = await file.read()
    metadata_service = MetadataService(metadata_dao=metadata_dao)
    await metadata_service.upload_metadata(
        exchange_name=exchange_name, content_type=file.content_type, data=data
    )

    return {"response": "Metadata uploaded successfully!"}
