import logging
from dataclasses import dataclass

from tools.retriever_tool import PolicyRetrieverTool
from tools.calculator_tool import LeaveNoticeCalculator
from tools.date_tool import CurrentDateTool

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


@dataclass
class AgentDependencies:
    """
    Shared dependencies used by the PydanticAI agent.
    """

    retriever: PolicyRetrieverTool
    calculator: LeaveNoticeCalculator
    date_tool: CurrentDateTool


def get_dependencies() -> AgentDependencies:
    """
    Create and return all shared dependencies.
    """

    logger.info("Initializing agent dependencies...")

    dependencies = AgentDependencies(
        retriever=PolicyRetrieverTool(),
        calculator=LeaveNoticeCalculator(),
        date_tool=CurrentDateTool(),
    )

    logger.info("Agent dependencies initialized successfully.")

    return dependencies