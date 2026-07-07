import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from predefined_data import get_predefined_habits
import analytics


@pytest.fixture
def habits():
    return get_predefined_habits()


def test_list_all_habits(habits):
    names = analytics.list_all_habits(habits)
    assert names == ["Drink 8 glasses of water", "Read 10 pages of a book", "Workout for 30 minutes", "Clean apartment", "Go for a walk"]


def test_longest_streak_perfect_daily_habit(habits):
    drink_water = next(h for h in habits if h.name == "Drink 8 glasses of water")
    assert analytics.longest_streak_for_habit(drink_water) == 28


def test_longest_streak_daily_habit_with_gap(habits):
    read_pages = next(h for h in habits if h.name == "Read 10 pages of a book")
    assert analytics.longest_streak_for_habit(read_pages) == 15


def test_longest_streak_weekly_habit_with_gap(habits):
    walk_habit = next(h for h in habits if h.name == "Go for a walk")
    assert analytics.longest_streak_for_habit(walk_habit) == 2


def test_longest_streak_overall(habits):
    assert analytics.longest_streak_overall(habits) == 28


def test_longest_streak_overall_empty_list():
    assert analytics.longest_streak_overall([]) == 0