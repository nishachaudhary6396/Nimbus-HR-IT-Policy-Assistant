import logging

logger = logging.getLogger(__name__)


class HallucinationGuard:
    """
    Prevents the agent from answering when
    retrieved documents are not relevant enough.
    """

    def __init__(self, threshold: float = 1.20):
        self.threshold = threshold

    def can_answer(self, results) -> bool:
        """
        Returns True if the retrieved documents
        are relevant enough.
        """

        # No documents found
        if not results:
            logger.warning("No documents retrieved.")
            return False

        # Best score (lowest distance = best match)
        best_score = results[0][1]

        logger.info(
            "Best similarity score: %.4f",
            best_score,
        )

        if best_score > self.threshold:
            logger.warning(
                "Hallucination guard blocked the response."
            )
            return False

        logger.info(
            "Hallucination guard passed."
        )

        return True

    def refusal_message(self) -> str:
        return (
            "I couldn't find reliable information in the "
            "Nimbus HR & IT policy documents."
        )