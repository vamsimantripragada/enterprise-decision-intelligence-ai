from rag.rag_service import RAGService

if __name__ == "__main__":
    rag = RAGService()

    sample_documents = [
        "Company HR policy requires all employees to complete compliance training annually.",
        "Market analysis shows increasing adoption of AI-driven automation in enterprise operations.",
        "Data privacy regulations require secure handling of personal information."
    ]

    rag.ingest_documents(sample_documents)

    print("Sample documents ingested successfully.")
