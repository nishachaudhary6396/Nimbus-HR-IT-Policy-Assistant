from indexing.loading import PDFLoader

loader = PDFLoader()
documents = loader.load_documents()

print(f"Documents Loaded: {len(documents)}")

if documents:
    print("\nFirst Page:\n")
    print(documents[0].page_content[:500])

    print("\nMetadata:\n")
    print(documents[0].metadata)
else:
    print("No documents were loaded.")