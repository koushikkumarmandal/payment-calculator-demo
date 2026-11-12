def calculate_discount(price: float, discount) -> float:
    """
    Calculate final price after discount.

    The original implementation assumed *discount* was always a numeric type and
    performed ``discount / 100`` directly. Web forms often send discount values as
    strings (e.g., "10" or "15%"), which caused a ``TypeError``. The function now
    normalises the input:

    * ``None`` → no discount.
    * ``int``/``float`` → used as‑is.
    * ``str`` → stripped of whitespace, optional trailing "%", then converted
      to ``float``.
    * Any other type raises a ``ValueError`` for clarity.
    """
    if discount is None:
        return float(price)

    # Normalise discount to a numeric value representing a percentage.
    if isinstance(discount, str):
        # Remove surrounding whitespace.
        discount_clean = discount.strip()
        # Remove a trailing percent sign if present.
        if discount_clean.endswith('%'):
            discount_clean = discount_clean[:-1]
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
    """Process a transaction and return a summary dictionary.

    * ``user_id`` – identifier of the user.
    * ``cart_total`` – original cart amount.
    * ``discount_code_val`` – optional discount (numeric or string) to be applied.
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
