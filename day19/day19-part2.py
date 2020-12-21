def read_input(in_file: str):
    rules = {}
    strings = []
    terminal_set = []
    with open(in_file, "r") as f:
        for line in f.readlines():

            if '"' in line:

                index, rule = line.split(":")
                literal = rule.replace('"', "")
                rules[index] = literal.strip()
                terminal_set.append(literal.strip())

            elif ":" in line:
                index, rule = line.split(":")
                current_rules = rule.split("|")
                rules[index] = [[x.strip() for x in current_rule.strip().split(" ")] for current_rule in current_rules]
            else:
                if line != "\n":
                    strings.append(line.strip())

    return rules, strings, terminal_set


sols = set()


def generate_all_matching(rules: dict, terminals: list, sol: list):
    global cnt_11_rule
    global cnt_8_rule
    is_final = True
    pos = 0
    while pos < len(sol):
        if sol[pos] not in terminals:
            is_final = False
            break
        pos += 1
    if is_final:
        sols.add("".join(sol[:]))
        return

    for rule in rules[sol[pos]]:

        last_sol = sol
        if rule not in terminals:
            sol = sol[:pos] + rule + sol[pos + 1 :]
        else:
            sol = sol[:pos] + [rule] + sol[pos + 1 :]

        generate_all_matching(rules, terminals, sol)
        sol = last_sol


in_file = "day19/in-day-19.txt"

rules, strings, terminal_set = read_input(in_file)
generate_all_matching(rules, terminal_set, ["0"])

print(sum([1 if string in sols else 0 for string in strings]))