from indexing.loading import PDFLoader
from indexing.splitting import DocumentSplitter

loader = PDFLoader()
documents = loader.load_documents()

splitter = DocumentSplitter()
chunks = splitter.split_documents(documents)

print(f"Pages Loaded : {len(documents)}")
print(f"Chunks Created : {len(chunks)}")

print("\nFirst Chunk\n")
print(chunks[0].page_content)

print("\nMetadata\n")
print(chunks[0].metadata)