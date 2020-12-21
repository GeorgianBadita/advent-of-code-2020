from typing import List, Tuple


def read_input(in_file: str) -> List[str]:
    with open(in_file, "r") as f:
        return [line.strip().replace(" ", "") for line in f.readlines()]


def get_number(pos: int, expression: str) -> Tuple[float, int]:
    num = 0
    while pos < len(expression) and ord("0") <= ord(expression[pos]) <= ord("9"):
        num = num * 10 + int(expression[pos])
        pos += 1

    return num if num > 0 else float("-inf"), pos


def compute_expression(expression: str) -> int:
    stack = []
    pos = 0
    while pos < len(expression):
        num, new_pos = get_number(pos, expression)

        if new_pos >= len(expression):
            break

        if expression[new_pos] == ")":
            stack.append(num)
            while new_pos < len(expression) and expression[new_pos] == ")":
                new_pos += 1
            pos = new_pos + 1
            continue

        if expression[new_pos] == "(":
            while new_pos < len(expression) and expression[new_pos] == "(":
                new_pos += 1
            if expression[new_pos - 2] == ")":
                stack.append(expression[new_pos - 1])

            num, new_pos = get_number(new_pos, expression)
            stack.append(num)
            stack.append(expression[new_pos])
            pos = new_pos + 1
            continue

        if not stack:
            stack.append(num)
            stack.append(expression[new_pos])
            pos = new_pos + 1
            continue

        op = stack.pop()
        op1 = stack.pop()
        stack.append(op1 * num if op == "*" else op1 + num)
        stack.append(expression[new_pos])
        pos = new_pos + 1
    print(stack)
    return stack


in_file = "day18/in-day-18.txt"

expressions = read_input(in_file)
sums = [compute_expression(expr) for expr in expressions]
# print(sums)
# print(sum(sums))