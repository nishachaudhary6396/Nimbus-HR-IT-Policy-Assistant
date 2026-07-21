import logging

from pydantic_ai import Agent, RunContext
from pydantic_ai.models.mistral import MistralModel

from agent.dependencies import (
    AgentDependencies,
    get_dependencies,
)
from agent.system_prompt import SYSTEM_PROMPT

logger = logging.getLogger(__name__)


# Create the Mistral model
model = MistralModel(
    model_name="mistral-large-latest",
)


# Create the PydanticAI agent
policy_agent = Agent(
    model=model,
    deps_type=AgentDependencies,
    system_prompt=SYSTEM_PROMPT,
)


@policy_agent.tool
def policy_search(
    ctx: RunContext[AgentDependencies],
    query: str,
) -> list[dict]:
    """
    Search the Nimbus HR & IT policy documents.
    """

    logger.info("Policy search tool invoked.")

    return ctx.deps.retriever.search(query)


@policy_agent.tool
def leave_calculator(
    ctx: RunContext[AgentDependencies],
    joining_date: str,
    current_date: str,
    accrual_rate: float,
) -> dict:
    """
    Calculate leave balance.
    """

    logger.info("Leave calculator tool invoked.")

    return ctx.deps.calculator.calculate_leave(
        joining_date=joining_date,
        current_date=current_date,
        accrual_rate=accrual_rate,
    )


@policy_agent.tool
def get_today(
    ctx: RunContext[AgentDependencies],
) -> str:
    """
    Return today's date.
    """

    logger.info("Date tool invoked.")

    return ctx.deps.date_tool.get_today()


if __name__ == "__main__":

    deps = get_dependencies()

    while True:

        question = input("\nAsk: ")

        if question.lower() == "exit":
            break

        result = policy_agent.run_sync(
            question,
            deps=deps,
        )

        print("\nAnswer:\n")
        print(result.output)