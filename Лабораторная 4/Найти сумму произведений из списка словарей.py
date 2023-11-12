# TODO решите задачу
import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    total_sum = 0.0

    for item in data:
        total_sum += item["score"] * item["weight"]

    total_sum = round(total_sum, 3)

    return total_sum

print(task())
