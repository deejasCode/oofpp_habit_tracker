from datetime import datetime, timedelta
from habit import Habit

_TODAY = datetime(2026, 6, 28, 20, 0, 0)
_FOUR_WEEKS_AGO = _TODAY - timedelta(weeks=4)


def _daily_completions(skip_days=()):
    return [
        _FOUR_WEEKS_AGO + timedelta(days=day, hours=9)
        for day in range(28)
        if day not in skip_days
    ]


def _weekly_completions(skip_weeks=()):
    return [
        _FOUR_WEEKS_AGO + timedelta(weeks=week, days=2, hours=15)
        for week in range(4)
        if week not in skip_weeks
    ]


def get_predefined_habits():
    return [
        Habit(
            name="Drink 8 glasses of water",
            periodicity="daily",
            created_at=_FOUR_WEEKS_AGO,
            completions=_daily_completions(),
        ),
        Habit(
            name="Read 10 pages of a book",
            periodicity="daily",
            created_at=_FOUR_WEEKS_AGO,
            completions=_daily_completions(skip_days=(15,)),
        ),
        Habit(
            name="Workout for 30 minutes",
            periodicity="daily",
            created_at=_FOUR_WEEKS_AGO,
            completions=_daily_completions(skip_days=(3, 4, 20)),
        ),
        Habit(
            name="Clean apartment",
            periodicity="weekly",
            created_at=_FOUR_WEEKS_AGO,
            completions=_weekly_completions(),
        ),
        Habit(
            name="Go for a walk",
            periodicity="weekly",
            created_at=_FOUR_WEEKS_AGO,
            completions=_weekly_completions(skip_weeks=(2,)),
        ),
    ]