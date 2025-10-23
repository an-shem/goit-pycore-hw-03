import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    for param in (min, max, quantity):
        if not isinstance(param, int):
            print("All parameters must be integers!")
            return []
    are_all_parameters_correct = (
        min >= 1 and max <= 1000 and min < max and quantity >= min and quantity <= max
    )
    if not are_all_parameters_correct:
        return []
    res = set()
    while len(res) != quantity:
        res.add(random.randint(min, max))
    return sorted(list(res))


print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 36, 5))
print(get_numbers_ticket(1, "36", 5))
print(get_numbers_ticket("one", 15, 5))
print(get_numbers_ticket(20, 15, 5))
print(get_numbers_ticket(1, 1500, 15))
print(get_numbers_ticket(-20, 15, 5))
