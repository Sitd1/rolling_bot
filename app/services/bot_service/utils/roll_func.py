import random


def roll_dice(start=1, stop=100):
    """Roll a dice."""
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("start and stop must be int")
    if start > stop:
        raise ValueError("start > stop")
    if start < 0 or stop < 0:
        raise ValueError("Values must be non-negative")
    if stop > 10_000:
        raise ValueError("Value must be less than 10_000")
    return random.randint(start, stop)


def get_yes_or_no():
    rng = random.randint(0, 1)
    return ('no', 'yes')[rng]


def get_coin():
    rng = random.randint(0, 1)
    return ('Орёл', 'Решка')[rng]
