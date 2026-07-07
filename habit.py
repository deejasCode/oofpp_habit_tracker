from datetime import datetime, timedelta

class Habit:
    VALID_PERIODICITIES = ("daily", "weekly")

    def __init__(self, name, periodicity, created_at=None, completions=None):
        if periodicity not in self.VALID_PERIODICITIES:
            raise ValueError(f"periodicity must be one of {self.VALID_PERIODICITIES}, got '{periodicity}'")
        
        self.name = name
        self.periodicity = periodicity
        self.created_at = created_at or datetime.now()
        self.completions = completions or []
    
    def check_off(self, timestamp=None):
        self.completions.append(timestamp or datetime.now())
    
    def period_length(self):
        return timedelta(days=1) if self.periodicity =="daily" else timedelta(days=7)
    
    def to_dict(self):
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at.isoformat(),
            "completions": [c.isoformat() for c in self.completions],
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            periodicity=data["periodicity"],
            created_at=datetime.fromisoformat(data["created_at"]),
            completions=[datetime.fromisoformat(c) for c in data["completions"]],
        )

    def __repr__(self):
        return f"Habit(name={self.name!r}, periodicity={self.periodicity!r}, completions={len(self.completions)})"