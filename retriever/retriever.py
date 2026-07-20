import logging

from langchain_chroma import Chroma

from indexing.embedding import EmbeddingModel

logger = logging.getLogger(__name__)


class PolicyRetriever:
    """
    Loads the existing Chroma vector database
    and provides a retriever for policy search.
    """

    def __init__(
        self,
        persist_directory: str = "chroma_db",
        k: int = 4,
    ):

        self.embedding_model = (
            EmbeddingModel().get_embeddings()
        )

        self.vector_store = Chroma(
            persist_directory=persist_directory,
            embedding_function=self.embedding_model,
        )

        self.retriever = self.vector_store.as_retriever(
            search_kwargs={
                "k": k
            }
        )

        logger.info(
            "Policy retriever initialized."
        )

    def retrieve(
        self,
        query: str,
    ):

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