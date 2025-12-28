def get_even_numbers(numbers: tuple[int]) -> tuple[int]:
    result = [i for i in numbers if i % 2 == 0]

    return tuple(result)

numbers = (3, 6, 7, 8, 10, 11)
print(get_even_numbers(numbers))