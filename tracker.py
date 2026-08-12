from habit import Habit
from storage import save_habits, load_habits


class HabitTracker:
    """Manages the full collection of a user's habits.

    Handles adding, deleting, finding, and checking off habits, as
    well as saving and loading them from persistent storage.
    """

    def __init__(self, habits=None):
        """Initialize a tracker, optionally with an existing list of habits.

        Args:
            habits: A list of Habit objects to start with. Defaults
                to an empty list.
        """
        self.habits = habits or []

    def add_habit(self, name, periodicity):
        """Create a new habit and add it to the tracker.

        Args:
            name: The task description for the new habit.
            periodicity: Either "daily" or "weekly".

        Returns:
            The newly created Habit object.

        Raises:
            ValueError: If a habit with this name already exists.
        """
        if self.get_habit(name) is not None:
            raise ValueError(f"A habit named '{name}' already exists.")
        habit = Habit(name=name, periodicity=periodicity)
        self.habits.append(habit)
        return habit

    def get_habit(self, name):
        """Find a habit by its name.

        Args:
            name: The habit name to look up.

        Returns:
            The matching Habit object, or None if not found.
        """
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
        """Mark a habit as completed.

        Args:
            name: The name of the habit to check off.
            timestamp: When it was completed. Defaults to now.

        Raises:
            ValueError: If no habit with that name exists.
        """
        habit = self.get_habit(name)
        if habit is None:
            raise ValueError(f"No habit named '{name}' found.")
        habit.check_off(timestamp)
    
    def save(self, filepath="data/habits.json"):
        """Persist all current habits to a JSON file.

        Args:
            filepath: Destination path for the JSON file.
        """
        save_habits(self.habits, filepath)

    def load(self, filepath="data/habits.json"):
        """Load habits from a JSON file, replacing the current collection.

        Args:
            filepath: Source path of the JSON file.
        """
        self.habits = load_habits(filepath)