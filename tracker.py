from habit import Habit
from storage import save_habits, load_habits


class HabitTracker:
    def __init__(self, habits=None):
        self.habits = habits or []

    def add_habit(self, name, periodicity):
        if self.get_habit(name) is not None:
            raise ValueError(f"A habit named '{name}' already exists.")
        habit = Habit(name=name, periodicity=periodicity)
        self.habits.append(habit)
        return habit

    def get_habit(self, name):
        for habit in self.habits:
            if habit.name == name:
                return habit
        return None

    def delete_habit(self, name):
        habit = self.get_habit(name)
        if habit is None:
            raise ValueError(f"No habit named '{name}' found.")
        self.habits.remove(habit)

    def check_off_habit(self, name, timestamp=None):
        habit = self.get_habit(name)
        if habit is None:
            raise ValueError(f"No habit named '{name}' found.")
        habit.check_off(timestamp)
    
    def save(self, filepath="data/habits.json"):
        save_habits(self.habits, filepath)

    def load(self, filepath="data/habits.json"):
        self.habits = load_habits(filepath)