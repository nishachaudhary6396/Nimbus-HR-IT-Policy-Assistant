from pathlib import Path
import logging

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document

logger = logging.getLogger(__name__)


class PDFLoader:
    """
    Loads all PDF files from the docs directory
    and returns them as LangChain Document objects.
    """

    def __init__(self, directory: str = "docs"):
        self.directory = Path(directory)

    def load_documents(self) -> list[Document]:

        if not self.directory.exists():
            raise FileNotFoundError(
                f"PDF directory '{self.directory}' does not exist."
            )

        pdf_files = sorted(self.directory.glob("*.pdf"))

        if len(pdf_files) == 0:
            logger.warning("No PDF files found in %s", self.directory)
            return []

        all_documents = []

        logger.info("Loading %d PDF files...", len(pdf_files))

        for file in pdf_files:

            try:
                pdf_loader = PyMuPDFLoader(str(file))
                pages = pdf_loader.load()

                valid_pages = 0

                for page in pages:

                    if page.page_content.strip() == "":
                        continue

                    page.metadata.update(
                        {
                            "source": file.name,
                            "page": page.metadata.get("page", 0) + 1,
                            "policy": file.stem,
                        }
                    )

                    all_documents.append(page)
                    valid_pages += 1

                logger.info(
                    "%s loaded successfully (%d pages)",
                    file.name,
                    valid_pages,
                )

            except Exception as error:
                logger.exception(
                    "Unable to load %s : %s",
                    file.name,
                    error,
                )

        logger.info(
            "Total pages loaded: %d",
            len(all_documents),
        )

        return all_documents