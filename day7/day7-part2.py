from typing import Dict, List, Set


def read_input(in_file) -> Dict[str, List[str]]:
    dct = {}

    with open(in_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "contain no other bags" in line:
                key = line.split("bags")[0]
                dct[key.strip()] = []
                continue
            left_side, right_side = line.split("contain")
            key = left_side.replace(" bags", "").strip()
            can_contain = right_side.split(",")
            for type_contain in can_contain:
                type_contain = type_contain.strip().replace(".", "")
                value = " ".join(type_contain.split(" ")[:-1])
                if key in dct:
                    dct[key].append(value)
                else:
                    dct[key] = [value]
    return dct


def dfs(node: str, graph: Dict[str, List[str]]) -> int:
    if node not in graph or not graph[node]:
        return 0
    needed_bags = 0
    for adj in graph[node]:
        split_adj = adj.split(" ")
        multiplier, node_id = int(split_adj[0]), " ".join(split_adj[1:])
        needed_bags += multiplier * dfs(node_id, graph) + multiplier
    return needed_bags


in_file = "day7/in-day-7.txt"
graph = read_input(in_file)
start_node = "shiny gold"

print(graph)
print(dfs(start_node, graph))
