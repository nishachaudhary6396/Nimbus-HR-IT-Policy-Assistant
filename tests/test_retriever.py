from retriever.retriever import PolicyRetriever


retriever = PolicyRetriever()

docs = retriever.retrieve(
    "How many earned leaves are allowed?"
)

for i, doc in enumerate(docs, start=1):
    print("=" * 50)
    print(f"Result {i}")
    print(doc.metadata)
    print(doc.page_content[:300])