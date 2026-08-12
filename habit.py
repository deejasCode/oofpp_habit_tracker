from datetime import datetime, timedelta

class Habit:
    """Represents a single habit that a user wants to track.

    A habit has a name, a periodicity (daily or weekly), a creation
    timestamp, and a list of timestamps recording each time the
    habit's task was completed.
    """
    VALID_PERIODICITIES = ("daily", "weekly")

    def __init__(self, name, periodicity, created_at=None, completions=None):
        """Initialise a new Habit.

        Args:
            name: A short description of the habit's task.
            periodicity: Either "daily" or "weekly".
            created_at: When the habit was created. 
               Defaults to now if not provided.
            completions: A list of timestamps for previous completions. 
               Defaults to an empty list if not provided.
            
        Raises:
            ValueError: If periodicity is not "daily" or "weekly"
        """
        if periodicity not in self.VALID_PERIODICITIES:
            raise ValueError(f"periodicity must be one of {self.VALID_PERIODICITIES}, got '{periodicity}'")
        
        self.name = name
        self.periodicity = periodicity
        self.created_at = created_at or datetime.now()
        self.completions = completions or []
    
    def check_off(self, timestamp=None):
        """Mark the habit as completed at the given time.

        Args:
            timestamp: When the task was completed. Defaults to now.
        """
        self.completions.append(timestamp or datetime.now())
    
    def period_length(self):
        """Return the length of one period for this habit.

        Returns:
            A timedelta of 1 day for daily habits, or 7 days for
            weekly habits.
        """
        return timedelta(days=1) if self.periodicity =="daily" else timedelta(days=7)
    
    def to_dict(self):
        """Convert this habit into a plain dictionary for JSON storage.

        Returns:
            A dictionary with the habit's name, periodicity, creation
            timestamp, and completion timestamps, all as strings.
        """
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at.isoformat(),
            "completions": [c.isoformat() for c in self.completions],
        }

    @classmethod
    def from_dict(cls, data):
        """Reconstruct a Habit from a dictionary produced by to_dict().

        Args:
            data: A dictionary as returned by to_dict().

        Returns:
            A new Habit instance with the same state.
        """
        return cls(
            name=data["name"],
            periodicity=data["periodicity"],
            created_at=datetime.fromisoformat(data["created_at"]),
            completions=[datetime.fromisoformat(c) for c in data["completions"]],
        )

    def __repr__(self):
        """Return a readable representation of the habit for debugging."""
        return f"Habit(name={self.name!r}, periodicity={self.periodicity!r}, completions={len(self.completions)})"