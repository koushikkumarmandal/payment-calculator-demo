def calculate_discount(price: float, discount) -> float:
    """Calculate the final price after applying a percentage discount.

    Args:
        price: The original price.
        discount: The discount which can be ``None``, a number, or a string
            representing a numeric percentage (e.g., "10" or "10%").

    Returns:
        The price after the discount is applied.
    """
    if discount is None:
        return float(price)

    # Normalise discount to a numeric value representing a percentage.
    if isinstance(discount, str):
        # Remove surrounding whitespace and optional percent sign.
        discount_clean = discount.strip().replace('%', '')
        try:
            discount_numeric = float(discount_clean)
        except ValueError as exc:
            raise ValueError(f"Discount string '{discount}' is not a valid number") from exc
    elif isinstance(discount, (int, float)):
        discount_numeric = float(discount)
    else:
        raise ValueError(f"Unsupported discount type: {type(discount)}")

    # Convert percentage to a fraction and apply it.
    discount_val = discount_numeric / 100.0
    return float(price) - (float(price) * discount_val)


def process_transaction(user_id: int, cart_total: float, discount_code_val=None):
    """Process a transaction, applying a discount if provided.

    Args:
        user_id: Identifier of the user.
        cart_total: The total amount before discount.
        discount_code_val: Optional discount value (same format accepted by
            ``calculate_discount``).

    Returns:
        A dictionary with transaction details.
    """
    # Determine the final amount after applying any discount.
    if discount_code_val is not None:
        final_amount = calculate_discount(cart_total, discount_code_val)
    else:
        final_amount = float(cart_total)

    return {
        "user_id": user_id,
        "original": float(cart_total),
        "final_amount": round(final_amount, 2),
        "status": "APPROVED",
    }
