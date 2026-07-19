from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document


DB_DIRECTORY = "vector_db"


def create_vector_store(chunks):
    """
    Create and save a Chroma vector database.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    documents = []

    for chunk in chunks:
        documents.append(
            Document(
                page_content=chunk["content"],
                metadata={
                    "source": chunk["filename"]
                }
            )
        )

    vectordb = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=DB_DIRECTORY
    )

    return vectordb