from rag.vector_store import VectorStore


class RAGService:
    def __init__(self):
        self.vector_store = VectorStore()

    def ingest_documents(self, documents: list[str]):
        self.vector_store.add_documents(documents)

    def retrieve_context(self, query: str) -> list[str]:
        return self.vector_store.search(query)
