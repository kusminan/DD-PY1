from random import randint


def get_unique_list_numbers() -> list[int]:
    unique_numbers = set()
    while len(unique_numbers) < 15:
        unique_numbers.update(randint(-10, 10) for _ in range(1))
    return list(unique_numbers)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
