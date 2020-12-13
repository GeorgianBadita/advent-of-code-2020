from typing import List, Union
from functools import reduce


def read_data(in_file: str) -> Union[int, List[str]]:
    with open(in_file, "r") as f:
        lines = f.readlines()
        return int(lines[0].strip()), [bus.strip() for bus in lines[1].split(",")]


def get_first_time_moment(bus_ids: List[str]) -> int:
    new_bus_ids = []
    moduli = []
    for i, bus_id in enumerate(bus_ids):
        if bus_id == "x":
            continue
        new_bus_ids.append(int(bus_id))
        moduli.append(int(bus_id) - i)

    return chinese_remainder(new_bus_ids, moduli)


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


in_file = "day13/in-day-13.txt"

_, bus_ids = read_data(in_file)

print(get_first_time_moment(bus_ids))