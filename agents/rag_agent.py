from utils.retriever import get_retriever
from utils.llm_client import get_llm

llm = get_llm()
retriever = get_retriever()


def ask_ai(question):
    """
    Answer questions using Retrieval-Augmented Generation (RAG).
    """

    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an AI Hospital Assistant.

Answer the question ONLY using the provided hospital policy documents.

If the answer is not present in the documents, reply:

"I couldn't find this information in the hospital policy documents."

Hospital Policy Documents:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content