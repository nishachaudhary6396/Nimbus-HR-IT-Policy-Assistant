from datetime import date


class CurrentDateTool:
    """
    Returns today's date.
    """

    @staticmethod
    def get_today() -> str:

        return date.today().strftime("%Y-%m-%d")