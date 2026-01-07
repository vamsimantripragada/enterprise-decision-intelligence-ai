import chromadb
from sentence_transformers import SentenceTransformer


class VectorStore:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(
            name="enterprise_docs"
        )
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

    def add_documents(self, docs: list[str]):
        embeddings = self.embedder.encode(docs).tolist()
        ids = [str(i) for i in range(len(docs))]

        self.collection.add(
            documents=docs,
            embeddings=embeddings,
            ids=ids
        )

    def search(self, query: str, top_k: int = 3) -> list[str]:
        query_embedding = self.embedder.encode([query]).tolist()

        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=top_k
        )

        return results.get("documents", [[]])[0]
