from typing import List


class PasswordConstruct:
    def __init__(self, low: int, high: int, char: str, password: str):
        self.low = low
        self.high = high
        self.char = char
        self.password = password

    def __str__(self):
        return f"Low: {self.low}\n High: {self.high}\n Char: {self.char}\n Password: {self.password}\n"


def read_input(in_file: str) -> List[PasswordConstruct]:
    result_list = []
    with open(in_file, "r") as f:
        for line in f.readlines():
            parts: str = line.strip().split(" ")
            low, high = int(parts[0].split("-")[0]), int(parts[0].split("-")[1])
            char = parts[1].split(":")[0]
            password = parts[2]
            result_list.append(PasswordConstruct(low, high, char, password))

    return result_list


def count_valid(password_constructs: List[PasswordConstruct]) -> int:
    count = 0
    for password_construct in password_constructs:
        low_index = password_construct.low
        high_index = password_construct.high
        count += (
            password_construct.password[low_index - 1] == password_construct.char
        ) ^ (password_construct.password[high_index - 1] == password_construct.char)
    return count


in_file = "day2/in-day2.txt"
password_constructs = read_input(in_file)
print(count_valid(password_constructs))
