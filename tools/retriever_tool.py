import logging

from guard.hallucination_guard import HallucinationGuard
from retriever.retriever import PolicyRetriever

logger = logging.getLogger(__name__)


class PolicyRetrieverTool:
    """
    Tool used by the agent to search the
    Nimbus HR & IT policy documents.
    """

    def __init__(self):

        self.retriever = PolicyRetriever()

        self.guard = HallucinationGuard()

    def search(
        self,
        query: str,
    ):
        """
        Search policy documents after
        validating retrieval quality.
        """

        logger.info(
            "Searching policy documents..."
        )

        results = self.retriever.retrieve_with_scores(
            query
        )

        if not self.guard.can_answer(results):

            return {
                "success": False,
                "message": self.guard.refusal_message(),
            }

        documents = []

        for document, score in results:

            documents.append(
                {
                    "content": document.page_content,
                    "metadata": document.metadata,
                    "score": round(score, 4),
                }
            )

        logger.info(
            "Returning %d document(s).",
            len(documents),
        )

        return {
            "success": True,
            "documents": documents,
        }