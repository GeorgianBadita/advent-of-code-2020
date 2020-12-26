from typing import List, Tuple


def read_input(in_file: str) -> List[str]:
    with open(in_file, "r") as f:
        return [line.strip().replace(" ", "") for line in f.readlines()]


def get_precedence(op: str) -> int:
    if op == "*":
        return 1

    if op == "+":
        return 2

    return 0


op_apply_map = {"+": lambda x, y: x + y, "*": lambda x, y: x * y}


def compute_expression(expression: str) -> int:

    val_stack = []
    ops_stack = []

    curr_pos = 0

    while curr_pos < len(expression):
        if expression[curr_pos] == "(":
            ops_stack.append("(")

        elif ord("0") <= ord(expression[curr_pos]) <= ord("9"):
            num = 0
            while curr_pos < len(expression) and ord("0") <= ord(expression[curr_pos]) <= ord("9"):
                num = num * 10 + int(expression[curr_pos])
                curr_pos += 1
            curr_pos -= 1
            val_stack.append(num)

        elif expression[curr_pos] == ")":
            while ops_stack and ops_stack[-1] != "(":
                op1 = val_stack.pop()
                op2 = val_stack.pop()
                op = ops_stack.pop()
                val_stack.append(op_apply_map[op](op1, op2))
            ops_stack.pop()
        else:
            while ops_stack and get_precedence(ops_stack[-1]) >= get_precedence(expression[curr_pos]):
                op1 = val_stack.pop()
                op2 = val_stack.pop()
                op = ops_stack.pop()
                val_stack.append(op_apply_map[op](op1, op2))
            ops_stack.append(expression[curr_pos])

        curr_pos += 1

    while ops_stack:
        op1 = val_stack.pop()
        op2 = val_stack.pop()
        op = ops_stack.pop()
        val_stack.append(op_apply_map[op](op1, op2))
    return val_stack[-1]


in_file = "day18/in-day-18.txt"

expressions = read_input(in_file)
res = [compute_expression(expr) for expr in expressions]

print(sum(res))