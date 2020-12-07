from typing import Dict, List


def read_input(in_file) -> Dict[str, List[str]]:
    dct = {}

    with open(in_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "contain no other bags" in line:
                continue
            left_side, right_side = line.split("contain")
            value = left_side.replace(" bags", "").strip()
            can_contain = right_side.split(",")
            for type_contain in can_contain:
                type_contain = type_contain.strip().replace(".", "")
                key = " ".join(type_contain.split(" ")[1:-1])
                if key in dct:
                    dct[key].append(value)
                else:
                    dct[key] = [value]
    return dct


def bfs(start_node: str, graph: Dict[str, List[str]]) -> List[str]:
    queue = [start_node]
    visited_set = {start_node}
    in_comp = []
    while queue:
        current_node = queue.pop(0)
        if current_node != start_node:
            in_comp.append(current_node)
        if current_node in graph:
            for node in graph[current_node]:
                if node not in visited_set:
                    visited_set.add(node)
                    queue.append(node)

    return in_comp


in_file = "day7/in-day-7.txt"
graph = read_input(in_file)
start_node = "shiny gold"

can_have_shiny = bfs(start_node, graph)
print(len(can_have_shiny))
