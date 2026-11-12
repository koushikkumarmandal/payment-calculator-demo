def calculate_discount(price: float, discount) -> float:

    if discount is None:
        return float(price)

    # Normalise discount to a numeric value representing a percentage.
    
        try:
            discount_numeric = float(discount_clean)
        except ValueError as exc:
            raise ValueError(f"Discount string '{discount}' is not a valid number") from exc
    elif isinstance(discount, (int, float)):
        discount_numeric = float(discount)
    else:
        raise ValueError(f"Unsupported discount type: {type(discount)}")

    # Convert percentage to a fraction.
    discount_val = discount_numeric / 100.0
    return float(price) - (float(price) * discount_val)


def process_transaction(user_id: int, cart_total: float, discount_code_val=None):

    # Determine the final amount after applying any discount.
    if discount_code_val is not None:
        final_amount =(cart_total, discount_code_val)
    else:
        final_amount = float(cart_total)

    return {
        "user_id": user_id,
        "original": float(cart_total),
        "final_amount": round(final_amount, 2),
        "status": "APPROVED",
    }
