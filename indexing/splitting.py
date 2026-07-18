from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

import logging

logger = logging.getLogger(__name__)


class DocumentSplitter:
    """
    Splits loaded PDF documents into smaller chunks
    while preserving metadata.
    """

    def __init__(
        self,
        chunk_size: int = 800,
        chunk_overlap: int = 150,
    ):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                "",
            ],
        )

    def split_documents(
        self,
        documents: list[Document],
    ) -> list[Document]:

        logger.info("Splitting documents into chunks...")

        chunks = self.text_splitter.split_documents(documents)

        logger.info(
            "Created %d chunks from %d pages.",
            len(chunks),
            len(documents),
        )

        return chunks