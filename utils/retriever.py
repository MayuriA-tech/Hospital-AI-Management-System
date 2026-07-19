from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

DB_DIRECTORY = "vector_db"


def get_retriever():
    """
    Load the vector database and return a retriever.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma(
        persist_directory=DB_DIRECTORY,
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever