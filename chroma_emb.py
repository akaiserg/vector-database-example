from chromadb.utils import embedding_functions


default_emb = embedding_functions.DefaultEmbeddingFunction()

name = "Andres"

embedding = default_emb(name)

print(embedding)