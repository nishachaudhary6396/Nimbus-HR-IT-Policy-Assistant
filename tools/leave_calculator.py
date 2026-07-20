from datetime import date, datetime
from langchain.tools import tool


def completed_months(
    joining_date: str,
    current_date: str,
) -> int:
    """
    Calculate completed months of service.
    Date format: YYYY-MM-DD
    """

    start = datetime.strptime(
        joining_date,
        "%Y-%m-%d",
    ).date()

    end = datetime.strptime(
        current_date,
        "%Y-%m-%d",
    ).date()

    months = (
        (end.year - start.year) * 12
        + (end.month - start.month)
    )

    if end.day < start.day:
        months -= 1

    return max(months, 0)


@tool
def leave_calculator(
    joining_date: str,
    current_date: str,
    accrual_rate: float,
) -> str:
    """
    Calculate earned leave based on completed
    months of service.
    """

    months = completed_months(
        joining_date,
        current_date,
    )

    leave_balance = months * accrual_rate

    return (
        f"Completed Months: {months}\n"
        f"Accrued Leave: {leave_balance} days"
    )