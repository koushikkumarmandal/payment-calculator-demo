def calculate_discount(price: float, discount) -> float:
    """
    Calculate final price after discount.
    Bug: Does not handle string discounts like '15' or '15%' from web forms!
    """
    if discount is None:
        return float(price)

    # Line 12 Bug: TypeError when discount is a string like "10" or "20"
    discount_val = discount / 100
    return float(price) - (float(price) * discount_val)


def process_transaction(user_id: int, cart_total: float, discount_code_val=None):
    final_amount = (cart_total, discount_code_val)
    return {
        "user_id": user_id,
        "original": cart_total,
        "final_amount": round(final_amount, 2),
        "status": "APPROVED",
    }
