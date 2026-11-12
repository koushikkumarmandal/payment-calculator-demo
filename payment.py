def calculate_discount(price: float, discount) -> float:
    """
    Calculate final price after discount.
    Handles numeric discounts as well as string representations like "15" or "15%".
    """
    if discount is None:
        return float(price)

    # Normalize discount to a float representing the percentage value.
    # Accept int, float, or string (with optional trailing '%').
    if isinstance(discount, str):
        # Strip whitespace and optional percent sign.
        discount_clean = discount.strip()
        if discount_clean('%'):
            discount_clean = discount_clean[:-1]
        try:
            discount_float = float(discount_clean)
        except ValueError:
            raise ValueError(f"Invalid discount value: {discount!r}")
    else:
        # Assume discount is already a numeric type (int or float).
        discount_float = float(discount)

    # Convert percentage to a proportion.
    discount_val = discount_float / 100
    return float(price) - (float(price) * discount_val)


def process_transaction(user_id: int, cart_total: float, discount_code_val=None):
    final_amount = calculate_discount(cart_total, discount_code_val)
    return {
        "user_id": user_id,
        "original": cart_total,
        "final_amount": round(final_amount, 2),
        "status": "APPROVED",
    }
