import logging

from langchain_chroma import Chroma
from langchain_core.documents import Document

from indexing.embedding import EmbeddingModel

logger = logging.getLogger(__name__)


class VectorStore:
    """
    Creates and manages the Chroma vector database.
    """

    def __init__(
        self,
        persist_directory: str = "chroma_db",
    ):
        self.persist_directory = persist_directory

        embedding_model = EmbeddingModel()

        self.vector_store = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=embedding_model.get_embeddings(),
        )

        logger.info(
            "Chroma vector store initialized."
        )

    def add_documents(
        self,
        documents: list[Document],
    ):

        logger.info(
            "Adding %d chunks to Chroma...",
            len(documents),
        )

        # Create a unique ID for every chunk
        ids = [
            f"{doc.metadata['source']}_{doc.metadata['page']}_{i}"
            for i, doc in enumerate(documents)
        ]

        self.vector_store.add_documents(
            documents=documents,
            ids=ids,
        )

        logger.info(
            "Documents successfully stored."
        )

    def get_vector_store(self):
        return self.vector_store


if __name__ == "__main__":

    from indexing.loading import PDFLoader
    from indexing.splitting import DocumentSplitter

    loader = PDFLoader()
    documents = loader.load_documents()

    splitter = DocumentSplitter()
    chunks = splitter.split_documents(documents)

    vector_store = VectorStore()
    vector_store.add_documents(chunks)

    print("Vector database created successfully!")