from payment import calculate_discount, process_transaction


def test_discount_number():
    assert calculate_discount(100, 10) == 90.0


def test_discount_string():
    # This will raise TypeError: unsupported operand type(s) for /: 'str' and 'int'
    assert calculate_discount(100, "10") == 90.0
