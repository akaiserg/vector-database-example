import chromadb

chroma_client = chromadb.Client()
from chromadb.utils import embedding_functions

default_emb = embedding_functions.DefaultEmbeddingFunction()

collection_name = "test_collection"

collection = chroma_client.get_or_create_collection(name=collection_name,embedding_function=default_emb)

documents = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "Hola, mundo!"},
    {"id": "doc3", "text": "Goodbye, world!"},
    {"id": "doc4", "text": "Chao, mundo!"},
]

for doc in documents:
    collection.upsert(ids=[doc["id"]], documents=[doc["text"]])

query_texts = "how are you?"


results = collection.query(query_texts=[query_texts], n_results=2)
print(results)


for idx, documents in enumerate(results["documents"][0]):
    doc_id = results["ids"][0][idx]
    distance = results["distances"][0][idx]
    print(f"Document ID: {doc_id}, Distance: {distance}")