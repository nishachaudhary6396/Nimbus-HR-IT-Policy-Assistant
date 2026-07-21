import logging

from retriever.retriever import PolicyRetriever

logger = logging.getLogger(__name__)


class PolicyRetrieverTool:
    """
    Handles retrieval from the Nimbus policy knowledge base.
    """

    def __init__(self):
        self.retriever = PolicyRetriever()

    def search(self, query: str) -> list[dict]:
        """
        Search the policy documents.

        Returns:
            A list of retrieved chunks with metadata.
        """

        logger.info("Searching policy documents...")

        documents = self.retriever.retrieve(query)

        results = []

        for doc in documents:

            results.append(
                {
                    "content": doc.page_content,
                    "source": doc.metadata.get(
                        "source",
                        "Unknown",
                    ),
                    "page": doc.metadata.get(
                        "page",
                        "Unknown",
                    ),
                }
            )

        logger.info(
            "Retrieved %d document(s).",
            len(results),
        )

        return results