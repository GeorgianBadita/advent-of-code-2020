from typing import List, Dict


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


def validate_passport(passport: Dict[str, str], required_fields) -> bool:
    return set(passport.keys()) == set(required_fields) or set(
        list(passport.keys()) + ["cid"]
    ) == set(required_fields)


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
