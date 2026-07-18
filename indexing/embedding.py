import logging

from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings

load_dotenv()

logger = logging.getLogger(__name__)


class EmbeddingModel:
    """
    Creates and manages the Cohere embedding model.
    """

    def __init__(self):
        self.embedding_model = CohereEmbeddings(
            model="embed-english-v3.0"
        )

        logger.info("Cohere embedding model initialized.")

    def get_embeddings(self):
        return self.embedding_model