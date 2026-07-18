from indexing.embedding import EmbeddingModel

embedding_model = EmbeddingModel()

embeddings = embedding_model.get_embeddings()

vector = embeddings.embed_query(
    "How many casual leaves are allowed?"
)

print(f"Embedding Dimension: {len(vector)}")

print(vector[:10])