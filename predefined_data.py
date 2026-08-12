from datetime import datetime, timedelta
from habit import Habit

_TODAY = datetime(2026, 6, 28, 20, 0, 0)
_FOUR_WEEKS_AGO = _TODAY - timedelta(weeks=4)


def _daily_completions(skip_days=()):
    """Generate one completion per day over 28 days.

    Args:
        skip_days: Day offsets (0-27) to deliberately leave uncompleted,
            used to create realistic gaps in the example data.

    Returns:
        A list of completion timestamps.
    """
    return [
        _FOUR_WEEKS_AGO + timedelta(days=day, hours=9)
        for day in range(28)
        if day not in skip_days
    ]


def _weekly_completions(skip_weeks=()):
    """Generate one completion per week over 4 weeks.

    Args:
        skip_weeks: Week offsets (0-3) to deliberately leave uncompleted.

    Returns:
        A list of completion timestamps.
    """
    return [
        _FOUR_WEEKS_AGO + timedelta(weeks=week, days=2, hours=15)
        for week in range(4)
        if week not in skip_weeks
    ]


def get_predefined_habits():
    """Build the 5 predefined habits with 4 weeks of example history.

    Returns:
        A list of ready-to-use Habit objects, including both daily
        and weekly habits with realistic completion patterns.
    """
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