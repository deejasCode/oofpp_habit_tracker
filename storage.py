import json
import os
from habit import Habit


def save_habits(habits, filepath="data/habits.json"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    data = [habit.to_dict() for habit in habits]
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_habits(filepath="data/habits.json"):
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Habit.from_dict(entry) for entry in data]