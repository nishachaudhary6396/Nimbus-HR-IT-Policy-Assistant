import logging

from indexing.loading import PDFLoader
from indexing.splitting import DocumentSplitter
from indexing.vector_store import VectorStore


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def main():

    logger.info("Starting document ingestion...")

    # Step 1: Load PDF documents
    loader = PDFLoader()
    documents = loader.load_documents()

    # Step 2: Split documents into chunks
    splitter = DocumentSplitter()
    chunks = splitter.split_documents(documents)

    # Step 3: Store chunks in Chroma
    vector_store = VectorStore()
    vector_store.add_documents(chunks)

    logger.info("Document ingestion completed successfully!")


if __name__ == "__main__":
    main()