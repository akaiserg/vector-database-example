import chromadb
from chromadb.utils import embedding_functions

default_ef = embedding_functions.DefaultEmbeddingFunction()
chroma_client = chromadb.PersistentClient(path="./db/chroma_persist")

collection = chroma_client.get_or_create_collection(
    "my_story", embedding_function=default_ef
)

documents = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "Hola, mundo!"},
    {"id": "doc3", "text": "Goodbye, world!"},
    {"id": "doc4", "text": "Chao, mundo!"},
    {"id": "doc5", "text": "LLM is a great tool!"},
]


for doc in documents:
    collection.upsert(
        ids=[doc["id"]],
        documents=[doc["text"]],
        metadatas=[{"source": "my_story"}],
    )

query_text = "What is the LLM"

results = collection.query(
    query_texts=[query_text],
    n_results=2
)

for idx, documents in enumerate(results["documents"][0]):
    doc_id = results["ids"][0][idx]
    distance = results["distances"][0][idx]
    print(f"Document ID: {doc_id}, Distance: {distance}")