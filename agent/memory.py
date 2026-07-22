from pydantic_ai.messages import ModelMessage


class ConversationMemory:
    """
    Stores conversation history for the agent.
    """

    def __init__(self):
        self.history: list[ModelMessage] = []

    def get_history(self) -> list[ModelMessage]:
        return self.history

    def update_history(self, messages: list[ModelMessage]) -> None:
        self.history.extend(messages)

    def clear(self) -> None:
        self.history.clear()