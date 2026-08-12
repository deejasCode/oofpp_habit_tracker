from tracker import HabitTracker
from predefined_data import get_predefined_habits
import analytics

DATA_FILE = "data/habits.json"

MENU = """
==== Habit Tracker ====
1. List all habits
2. List habits by periodicity
3. Add a new habit
4. Check off a habit (mark as done today)
5. Delete a habit
6. Show longest streak for a habit
7. Show longest streak overall
9. Load predefined example habits
0. Save & exit
========================
"""


def run():
    """Run the interactive command-line menu.

    Loads saved habits, shows the menu, and handles user choices
    until they save and exit.
   """
    tracker = HabitTracker()
    tracker.load(DATA_FILE)

    while True:
        print(MENU)
        choice = input("Choose an option from the menu: ").strip()

        if choice == "1":
            for name in analytics.list_all_habits(tracker.habits):
                print(f" - {name}")
        elif choice == "2":
            periodicity = input("Which periodicity do you want to select? (daily/weekly): ").strip().lower()
            for name in analytics.list_habits_by_periodicity(tracker.habits, periodicity):
                print(f" - {name}")
        elif choice == "3":
            name = input("Habit name: ").strip()
            periodicity = input("Periodicity (daily/weekly): ").strip().lower()
            try:
                tracker.add_habit(name, periodicity)
                print(f"Added '{name}'.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "4":
            name = input("Which habit did you complete?: ").strip()
            try:
                tracker.check_off_habit(name)
                print(f"'{name}' checked off!")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "5":
            name = input("Which habit do you want to delete?: ").strip()
            try:
                tracker.delete_habit(name)
                print(f"Deleted '{name}'.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "6":
            name = input("Which habit?: ").strip()
            habit = tracker.get_habit(name)
            if habit is None:
                print(f"No habit named '{name}' found.")
            else:
                print(analytics.longest_streak_for_habit(habit))
        elif choice == "7":
            print(analytics.longest_streak_overall(tracker.habits))
        elif choice == "9":
            tracker.habits = get_predefined_habits()
            print("Loaded 5 predefined habits.")
        elif choice == "0":
            tracker.save(DATA_FILE)
            print("Saved everything. Goodbye!")
            break
        else:
            print("Not a valid option.")