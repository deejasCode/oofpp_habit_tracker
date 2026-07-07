from functools import reduce
from datetime import timedelta


def list_all_habits(habits):
    return list(map(lambda h: h.name, habits))


def list_habits_by_periodicity(habits, periodicity):
    matching = filter(lambda h: h.periodicity == periodicity, habits)
    return list(map(lambda h: h.name, matching))


def _period_start(timestamp, periodicity):
    if periodicity == "daily":
        return timestamp.date()
    iso_year, iso_week, _ = timestamp.isocalendar()
    return (iso_year, iso_week)


def _longest_streak_from_periods(sorted_periods, periodicity):
    if not sorted_periods:
        return 0

    def is_consecutive(previous, current):
        if periodicity == "daily":
            return current == previous + timedelta(days=1)
        prev_year, prev_week = previous
        cur_year, cur_week = current
        if prev_year == cur_year:
            return cur_week == prev_week + 1
        return prev_week >= 52 and cur_year == prev_year + 1 and cur_week == 1

    def accumulate(state, current_period):
        longest, current_run, previous = state
        if previous is not None and is_consecutive(previous, current_period):
            current_run += 1
        else:
            current_run = 1
        longest = max(longest, current_run)
        return (longest, current_run, current_period)

    initial_state = (0, 0, None)
    longest, _, _ = reduce(accumulate, sorted_periods, initial_state)
    return longest


def longest_streak_for_habit(habit):
    periods = sorted(set(
        map(lambda ts: _period_start(ts, habit.periodicity), habit.completions)
    ))
    return _longest_streak_from_periods(periods, habit.periodicity)


def longest_streak_overall(habits):
    if not habits:
        return 0
    streaks = map(longest_streak_for_habit, habits)
    return reduce(max, streaks, 0)