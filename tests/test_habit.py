import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from datetime import datetime
from habit import Habit


def test_create_daily_habit():
    habit = Habit(name="Drink 8 glasses of water", periodicity="daily")
    assert habit.name == "Drink 8 glasses of water"
    assert habit.periodicity == "daily"
    assert habit.completions == []


def test_invalid_periodicity_raises():
    with pytest.raises(ValueError):
        Habit(name="Bad habit", periodicity="monthly")


def test_check_off_adds_completion():
    habit = Habit(name="Workout", periodicity="daily")
    habit.check_off(datetime(2026, 1, 1, 8, 0))
    assert len(habit.completions) == 1
    assert habit.completions[0] == datetime(2026, 1, 1, 8, 0)


def test_check_off_defaults_to_now():
    habit = Habit(name="Workout", periodicity="daily")
    habit.check_off()
    assert len(habit.completions) == 1
    assert isinstance(habit.completions[0], datetime)


def test_period_length_daily():
    habit = Habit(name="Water", periodicity="daily")
    assert habit.period_length().days == 1


def test_period_length_weekly():
    habit = Habit(name="Clean", periodicity="weekly")
    assert habit.period_length().days == 7


def test_to_dict_and_from_dict_roundtrip():
    original = Habit(
        name="Read",
        periodicity="daily",
        created_at=datetime(2026, 1, 1, 10, 0),
        completions=[datetime(2026, 1, 1, 20, 0), datetime(2026, 1, 2, 20, 0)],
    )
    data = original.to_dict()
    restored = Habit.from_dict(data)

    assert restored.name == original.name
    assert restored.periodicity == original.periodicity
    assert restored.created_at == original.created_at
    assert restored.completions == original.completions