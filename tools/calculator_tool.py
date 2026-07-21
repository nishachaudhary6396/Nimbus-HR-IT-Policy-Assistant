from datetime import datetime


class LeaveNoticeCalculator:
    """
    Performs leave and notice period calculations.
    """

    @staticmethod
    def completed_months(
        joining_date: str,
        current_date: str,
    ) -> int:

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

    def calculate_leave(
        self,
        joining_date: str,
        current_date: str,
        accrual_rate: float,
    ) -> dict:

        months = self.completed_months(
            joining_date,
            current_date,
        )

        leave_balance = months * accrual_rate

        return {
            "completed_months": months,
            "leave_balance": leave_balance,
        }