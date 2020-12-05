from typing import List, Dict
from functools import reduce


def read_passports(in_file: str) -> List[Dict[str, str]]:
    passports = []

    with open(in_file, "r") as f:
        current_passport = {}
        for line in f.readlines():
            if line == "\n":
                passports.append(current_passport)
                current_passport = {}
            else:

                line = line.replace("\n", "").replace(" ", "\n")
                for item in line.split("\n"):
                    split_item = item.split(":")
                    current_passport[split_item[0].strip()] = split_item[1].strip()
        passports.append(current_passport)
        return passports


# This can be split in functions for each field, or regex but it's 00:00 and I'm too tired
def validate_passport(passport: Dict[str, str], required_fields) -> bool:
    if not (
        set(passport.keys()) == set(required_fields)
        or set(list(passport.keys()) + ["cid"]) == set(required_fields)
    ):
        return False

    is_valid = True
    try:
        byr = int(passport["byr"])
        is_valid = 1920 <= byr <= 2002
    except ValueError:
        is_valid = False

    if not is_valid:
        return False

    try:
        iyr = int(passport["iyr"])
        is_valid = 2010 <= iyr <= 2020
    except ValueError:
        is_valid = False

    if not is_valid:
        return False

    try:
        eyr = int(passport["eyr"])
        is_valid = 2020 <= eyr <= 2030
    except ValueError:
        is_valid = False

    if not is_valid:
        return False

    try:
        hgt = passport["hgt"]
        is_valid = hgt[-2:] == "cm" or hgt[-2:] == "in"
        if not is_valid:
            return False
        hgt_val = int(hgt[:-2])
        if hgt[-2:] == "cm":
            is_valid = 150 <= hgt_val <= 193
        else:
            is_valid = 59 <= hgt_val <= 76
        if not is_valid:
            return False
    except ValueError:
        is_valid = False

    hcl = passport["hcl"]
    if hcl[0] != "#" or hcl.count("#") > 1:
        return False

    is_valid = len(hcl) == 7 and reduce(
        lambda x, y: x and (y in "abcdef0123456789"), list(hcl[1:]), True
    )
    if not is_valid:
        return False

    is_valid = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    if not is_valid:
        return False

    is_valid = len(passport["pid"]) == 9 and reduce(
        lambda x, y: x and (y in "0123456789"), passport["pid"], True
    )
    return is_valid


in_file = "day4/in-day-4.txt"

passports = read_passports(in_file)

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]


print(
    len(
        [
            passport
            for passport in passports
            if validate_passport(passport, required_fields)
        ]
    )
)
