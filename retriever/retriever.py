import logging

from langchain_chroma import Chroma

from indexing.embedding import EmbeddingModel

logger = logging.getLogger(__name__)


class PolicyRetriever:
    """
    Loads the existing Chroma vector database
    and provides methods for policy search.
    """

    def __init__(
        self,
        persist_directory: str = "chroma_db",
        k: int = 4,
    ):

        self.k = k

        self.embedding_model = (
            EmbeddingModel().get_embeddings()
        )

        self.vector_store = Chroma(
            persist_directory=persist_directory,
            embedding_function=self.embedding_model,
        )

        self.retriever = self.vector_store.as_retriever(
            search_kwargs={
                "k": self.k
            }
        )

        logger.info(
            "Policy retriever initialized."
        )

    def retrieve(
        self,
        query: str,
    ):
        """
        Retrieve relevant policy documents.
        """

        logger.info(
            "Searching for: %s",
            query,
        )

        documents = self.retriever.invoke(query)

        logger.info(
            "Retrieved %d document(s).",
            len(documents),
        )

        return documents

    def retrieve_with_scores(
        self,
        query: str,
    ):
        """
        Retrieve documents along with similarity scores.
        """

        logger.info(
            "Searching with similarity scores for: %s",
            query,
        )

        results = self.vector_store.similarity_search_with_score(
            query,
            k=self.k,
        )

        logger.info(
            "Retrieved %d scored document(s).",
            len(results),
        )

        for i, (_, score) in enumerate(results, start=1):
            logger.info(
                "Result %d score: %.4f",
                i,
                score,
            )

        return results