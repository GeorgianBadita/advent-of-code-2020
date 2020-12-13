from typing import List, Union


def read_data(in_file: str) -> Union[int, List[str]]:
    with open(in_file, "r") as f:
        lines = f.readlines()
        return int(lines[0].strip()), [bus.strip() for bus in lines[1].split(",")]


def get_best_bus(time: int, bus_ids: List[str]) -> int:
    new_bus_ids = [int(bus_id) for bus_id in bus_ids if bus_id != "x"]

    bus_times = [
        (bus_id * (time // bus_id + 1), bus_id) if time % bus_id != 0 else (time, bus_id) for bus_id in new_bus_ids
    ]
    bus_times = sorted(bus_times, key=lambda x: x[0])
    return (bus_times[0][0] - time) * bus_times[0][1]


in_file = "day13/in-day-13.txt"

time, bus_ids = read_data(in_file)

print(get_best_bus(time, bus_ids))