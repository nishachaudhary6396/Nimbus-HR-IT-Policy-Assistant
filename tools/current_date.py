from datetime import date

from langchain.tools import tool


@tool
def get_current_date() -> str:
    """
    Returns today's date in YYYY-MM-DD format.
    Use this whenever the user asks about
    'today', 'current date', or date-based calculations.
    """

    return date.today().strftime("%Y-%m-%d")