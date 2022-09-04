from src.transformer.blockchain_order_book_transformer import BlockChainOrderBookTransformer
from tests.mock.order_book import order_book_list, order_book_list_transformed, order_book_list_transformed_filtered_asks, order_book_list_transformed_filtered_bids, order_book_list_transformed_descending_symbol, order_book_list_transformed_descending_symbol_filtered_asks, order_book_list_transformed_descending_symbol_filtered_bids
import pytest
import json

class TestBlockChainOrderBookTransformer:
    @pytest.fixture
    def order_book(self):
        return order_book_list()[0]
    
    @pytest.fixture
    def order_book_list(self):
        return order_book_list()

    def test_map_to_order_book(self, order_book):
        blockchain_order_book_transformer = BlockChainOrderBookTransformer()
        expected = {
            "symbol": "BTC-USD",
            "bids": [
                {"price": 20000, "quantity": 0.1, "num_orders": 1000},
                {"price": 19999, "quantity": 0.2, "num_orders": 2000},
            ],
            "asks": [
                {"price": 20005, "quantity": 0.1, "num_orders": 1000},
                {"price": 20003, "quantity": 0.2, "num_orders": 2000},
            ]
        }

        res = blockchain_order_book_transformer.map_to_order_book(order_book=order_book)

        assert res == expected

    def test_process_order_book_ascending(self, order_book_list):
        blockchain_order_book_transformer = BlockChainOrderBookTransformer()

        res = blockchain_order_book_transformer.process_order_book(order_books_list=order_book_list)

        assert res == order_book_list_transformed

    def test_process_order_book_descending(self, order_book_list):
        blockchain_order_book_transformer = BlockChainOrderBookTransformer()

        res = blockchain_order_book_transformer.process_order_book(order_books_list=order_book_list, sort_symbol_order="desc")

        assert res == order_book_list_transformed_descending_symbol
    
    def test_filter_order_book(self, order_book_list):
        blockchain_order_book_transformer = BlockChainOrderBookTransformer()

        expected = [
            {
                "symbol": "BTC-USD",
                "bids": [
                    {"px": 20000, "qty": 0.1, "num": 1000},
                    {"px": 19999, "qty": 0.2, "num": 2000},
                ],
                "asks": [
                    {"px": 20005, "qty": 0.1, "num": 1000},
                    {"px": 20003, "qty": 0.2, "num": 2000},
                ]
            },
            {
                "symbol": "ETH-USD",
                "bids": [
                    {"px": 1500, "qty": 1, "num": 1000},
                    {"px": 1499, "qty": 2, "num": 2000},
                ],
                "asks": [
                    {"px": 1510, "qty": 1, "num": 1000},
                    {"px": 1505, "qty": 2, "num": 2000},
                ],
            }
        ]

        res = blockchain_order_book_transformer.filter_order_book(order_books_list=order_book_list)

        assert res == expected

    def test_filter_order_book_bids(self, order_book_list):
        blockchain_order_book_transformer = BlockChainOrderBookTransformer()

        expected = [
            {
                "symbol": "BTC-USD",
                "bids": [
                    {"px": 20000, "qty": 0.1, "num": 1000},
                    {"px": 19999, "qty": 0.2, "num": 2000},
                ]
            },
            {
                "symbol": "ETH-USD",
                "bids": [
                    {"px": 1500, "qty": 1, "num": 1000},
                    {"px": 1499, "qty": 2, "num": 2000},
                ]
            }
        ]

        res = blockchain_order_book_transformer.filter_order_book(order_books_list=order_book_list, order_type="bid")

        assert res == expected

    def test_filter_order_book_asks(self, order_book_list):
        blockchain_order_book_transformer = BlockChainOrderBookTransformer()

        expected = [
            {
                "symbol": "BTC-USD",
                "asks": [
                    {"px": 20005, "qty": 0.1, "num": 1000},
                    {"px": 20003, "qty": 0.2, "num": 2000},
                ]
            },
            {
                "symbol": "ETH-USD",
                "asks": [
                    {"px": 1510, "qty": 1, "num": 1000},
                    {"px": 1505, "qty": 2, "num": 2000},
                ],
            }
        ]

        res = blockchain_order_book_transformer.filter_order_book(order_books_list=order_book_list, order_type="ask")

        assert res == expected    
        
    def test_transform_order_book(self, order_book_list):
        blockchain_order_book_transformer = BlockChainOrderBookTransformer()

        res = blockchain_order_book_transformer.transform_order_book(order_book_list=order_book_list)

        assert res == order_book_list_transformed

    def test_transform_order_book_invalid_order_type(self, order_book_list):
        blockchain_order_book_transformer = BlockChainOrderBookTransformer()

        res = blockchain_order_book_transformer.transform_order_book(order_book_list=order_book_list, order_type="invalid")

        assert res == []

    def test_transform_order_book_filter_bids(self, order_book_list):
        blockchain_order_book_transformer = BlockChainOrderBookTransformer()

        res = blockchain_order_book_transformer.transform_order_book(order_book_list=order_book_list, order_type="bid")

        assert res == order_book_list_transformed_filtered_bids

    def test_transform_order_book_filter_asks(self, order_book_list):
        blockchain_order_book_transformer = BlockChainOrderBookTransformer()

        res = blockchain_order_book_transformer.transform_order_book(order_book_list=order_book_list, order_type="ask")

        assert res == order_book_list_transformed_filtered_asks

    def test_transform_order_book_descending(self, order_book_list):
        blockchain_order_book_transformer = BlockChainOrderBookTransformer()

        res = blockchain_order_book_transformer.transform_order_book(order_book_list=order_book_list, sort_symbol_order="desc")

        assert res == order_book_list_transformed_descending_symbol

    def test_transform_order_book_descending_filter_asks(self, order_book_list):
        blockchain_order_book_transformer = BlockChainOrderBookTransformer()

        res = blockchain_order_book_transformer.transform_order_book(order_book_list=order_book_list, sort_symbol_order="desc", order_type="ask")

        assert res == order_book_list_transformed_descending_symbol_filtered_asks

    def test_transform_order_book_descending_filter_bids(self, order_book_list):
        blockchain_order_book_transformer = BlockChainOrderBookTransformer()

        res = blockchain_order_book_transformer.transform_order_book(order_book_list=order_book_list, sort_symbol_order="desc", order_type="bid")

        assert res == order_book_list_transformed_descending_symbol_filtered_bids


