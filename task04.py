def get_even_order(orders: list[tuple]) -> list[tuple]:
    result = []
    for order, name in orders:
        if order % 2 == 0:
            result.append((order, name))

    return result

orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]
print(get_even_order(orders=orders))