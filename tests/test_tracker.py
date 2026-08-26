import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from tracker import HabitTracker


def test_add_habit_creates_habit():
    tracker = HabitTracker()
    habit = tracker.add_habit("Meditate", "daily")
    assert habit.name == "Meditate"
    assert habit.periodicity == "daily"
    assert len(tracker.habits) == 1


def test_add_habit_duplicate_name_raises():
    tracker = HabitTracker()
    tracker.add_habit("Meditate", "daily")
    with pytest.raises(ValueError):
        tracker.add_habit("Meditate", "weekly")


def test_delete_habit_removes_it():
    tracker = HabitTracker()
    tracker.add_habit("Meditate", "daily")
    tracker.delete_habit("Meditate")
    assert len(tracker.habits) == 0


def test_delete_nonexistent_habit_raises():
    tracker = HabitTracker()
    with pytest.raises(ValueError):
        tracker.delete_habit("Doesn't exist")


def test_check_off_habit_adds_completion():
    tracker = HabitTracker()
    tracker.add_habit("Meditate", "daily")
    tracker.check_off_habit("Meditate")
    habit = tracker.get_habit("Meditate")
    assert len(habit.completions) == 1


def test_check_off_nonexistent_habit_raises():
    tracker = HabitTracker()
    with pytest.raises(ValueError):
        tracker.check_off_habit("Doesn't exist")


def test_get_habit_returns_none_if_not_found():
    tracker = HabitTracker()
    assert tracker.get_habit("Nothing here") is None