from typing import Any

def order_book_list() -> list[Any]:
    return [
    {
        "symbol": "BTC-USD",
        "bids": [
            {"px": 20000, "qty": 0.1, "num": 1000},
            {"px": 19999, "qty": 0.2, "num": 2000},
        ],
        "asks": [
            {"px": 20005, "qty": 0.1, "num": 1000},
            {"px": 20003, "qty": 0.2, "num": 2000},
        ],
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
        ]
    }
]

order_book_list_transformed = [
    {
        "symbol": "BTC-USD",
        "bids": [
            {"price": 20000, "quantity": 0.1, "num_orders": 1000},
            {"price": 19999, "quantity": 0.2, "num_orders": 2000},
        ],
        "asks": [
            {"price": 20005, "quantity": 0.1, "num_orders": 1000},
            {"price": 20003, "quantity": 0.2, "num_orders": 2000},
        ]
    },
    {
        "symbol": "ETH-USD",
        "bids": [
            {"price": 1500, "quantity": 1, "num_orders": 1000},
            {"price": 1499, "quantity": 2, "num_orders": 2000},
        ],
        "asks": [
            {"price": 1510, "quantity": 1, "num_orders": 1000},
            {"price": 1505, "quantity": 2, "num_orders": 2000},
        ],
    }
]

order_book_list_transformed_filtered_bids = [
    {
        "symbol": "BTC-USD",
        "bids": [
            {"price": 20000, "quantity": 0.1, "num_orders": 1000},
            {"price": 19999, "quantity": 0.2, "num_orders": 2000},
        ],
    },
    {
        "symbol": "ETH-USD",
        "bids": [
            {"price": 1500, "quantity": 1, "num_orders": 1000},
            {"price": 1499, "quantity": 2, "num_orders": 2000},
        ],

    }
]

order_book_list_transformed_filtered_asks = [
    {
        "symbol": "BTC-USD",
        "asks": [
            {"price": 20005, "quantity": 0.1, "num_orders": 1000},
            {"price": 20003, "quantity": 0.2, "num_orders": 2000},
        ]
    },
    {
        "symbol": "ETH-USD",
          "asks": [
            {"price": 1510, "quantity": 1, "num_orders": 1000},
            {"price": 1505, "quantity": 2, "num_orders": 2000},
        ],
    }
]

order_book_list_transformed_descending_symbol = [
    {
        "symbol": "ETH-USD",
        "bids": [
            {"price": 1500, "quantity": 1, "num_orders": 1000},
            {"price": 1499, "quantity": 2, "num_orders": 2000},
        ],
        "asks": [
            {"price": 1510, "quantity": 1, "num_orders": 1000},
            {"price": 1505, "quantity": 2, "num_orders": 2000},
        ],
    },
    {
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
]

order_book_list_transformed_descending_symbol_filtered_asks= [
    {
        "symbol": "ETH-USD",
        "asks": [
            {"price": 1510, "quantity": 1, "num_orders": 1000},
            {"price": 1505, "quantity": 2, "num_orders": 2000},
        ],
    },
    {
        "symbol": "BTC-USD",
        "asks": [
            {"price": 20005, "quantity": 0.1, "num_orders": 1000},
            {"price": 20003, "quantity": 0.2, "num_orders": 2000},
        ]
    }
]

order_book_list_transformed_descending_symbol_filtered_bids= [
    {
        "symbol": "ETH-USD",
        "bids": [
            {"price": 1500, "quantity": 1, "num_orders": 1000},
            {"price": 1499, "quantity": 2, "num_orders": 2000},
        ],
    },
    {
        "symbol": "BTC-USD",
        "bids": [
            {"price": 20000, "quantity": 0.1, "num_orders": 1000},
            {"price": 19999, "quantity": 0.2, "num_orders": 2000},
        ],
    }
]