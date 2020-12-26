from typing import List, Tuple


def read_input(in_file: str) -> List[str]:
    with open(in_file, "r") as f:
        return [line.strip().replace(" ", "") for line in f.readlines()]


def get_number(pos: int, expression: str) -> Tuple[float, int]:

    if not (ord("0") <= ord(expression[pos]) <= ord("9")):
        return float("-inf"), pos

    num = 0
    while pos < len(expression) and ord("0") <= ord(expression[pos]) <= ord("9"):
        num = num * 10 + int(expression[pos])
        pos += 1

    return num, pos


def get_closing_par_pos(stack: list) -> int:
    pos = len(stack) - 1
    count = 1
    while pos >= 0:
        if stack[pos] == "(":
            count += 1
        elif stack[pos] == ")":
            count -= 1
        if count == 0:
            break
        pos -= 1

    return pos


def compute_expression(expression: str) -> int:
    pos = 0
    stack = []
    while pos < len(expression):
        num, next_pos = get_number(pos, expression)
        if num != float("-inf"):
            stack.append(num)
        if next_pos < len(expression):
            stack.append(expression[next_pos])
        pos = next_pos + 1
    stack.reverse()
    while len(stack) != 1:
        op1 = stack.pop()
        if op1 == "(":
            ending_par_pos = get_closing_par_pos(stack)
            stack = stack[:ending_par_pos] + stack[ending_par_pos + 1 :]
            continue
        op = stack.pop()
        op2 = stack.pop()
        if op2 == "(":
            ending_par_pos = get_closing_par_pos(stack)
            stack = stack[:ending_par_pos] + [op1, op] + stack[ending_par_pos + 1 :]
        else:
            if op == "+":
                stack.append(op1 + op2)
            else:
                stack.append(op1 * op2)

    return stack[-1]


in_file = "day18/in-day-18.txt"

expressions = read_input(in_file)
res = [compute_expression(expr) for expr in expressions]
print(sum(res))