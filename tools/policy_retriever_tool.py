import logging

from langchain.tools import tool

from retriever.retriever import PolicyRetriever

logger = logging.getLogger(__name__)

# Create one retriever instance
policy_retriever = PolicyRetriever()


@tool
def policy_search(query: str) -> str:
    """
    Search the Nimbus HR & IT policy documents.

    Use this tool whenever the user asks about
    company policies, leave, attendance,
    expenses, IT security, remote work,
    code of conduct, or employee benefits.
    """

    logger.info("Policy search tool called.")

    documents = policy_retriever.retrieve(query)

    if not documents:
        return (
            "I couldn't find any relevant information "
            "in the Nimbus policy documents."
        )

    results = []

    for doc in documents:

        source = doc.metadata.get(
            "source",
            "Unknown Document",
        )

        page = doc.metadata.get(
            "page",
            "Unknown",
        )

        text = doc.page_content.strip()

        results.append(
            f"Source: {source} | Page: {page}\n{text}"
        )

    return "\n\n" + ("-" * 50) + "\n\n".join(results)