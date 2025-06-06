import logging
from typing import Dict

logger = logging.getLogger(__name__)


class Order:
    def __init__(self, customer_type: str, amount: float, items: int):
        self.customer_type = customer_type
        self.amount = amount
        self.items = items

    def to_dict(self) -> Dict:
        return {
            "customer_type": self.customer_type,
            "amount": self.amount,
            "items": self.items
        }


def calculate_discount(order: Dict) -> float:
    is_vip = order["customer_type"] == "VIP"
    is_large_order = order["amount"] > 1000 and order["items"] > 5
    is_regular = order["customer_type"] == "Regular"
    is_medium_order = order["amount"] > 500

    logger.debug(f"Evaluating discount for: {order}")

    if is_vip and is_large_order:
        logger.info("VIP large order discount applied.")
        return order["amount"] * 0.9
    elif is_regular and is_medium_order:
        logger.info("Regular medium order discount applied.")
        return order["amount"] * 0.95
    else:
        logger.info("No discount applied.")
        return order["amount"]


def main():
    orders = [
        Order("VIP", 1500, 6),
        Order("Regular", 600, 2),
        Order("Guest", 200, 1),
    ]

    for o in orders:
        discount_price = calculate_discount(o.to_dict())
        print(f"Final price: {discount_price:.2f}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
