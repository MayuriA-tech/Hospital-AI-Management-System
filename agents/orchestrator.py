from utils.llm_client import get_llm
from agents.sql_agent import ask_database
from agents.rag_agent import ask_ai

llm = get_llm()


def classify_query(question):
    """
    Classify the user's question as SQL or RAG.
    """

    prompt = f"""
You are an intelligent routing agent.

Your job is to classify the user's question into ONE category.

Category 1: SQL
Use SQL when the question is about:
- Patient records
- Patient names
- Age
- Gender
- Blood Type
- Medical Condition
- Doctor
- Hospital
- Billing Amount
- Insurance Provider
- Admission Type
- Room Number
- Medication
- Test Results
- Admission Date
- Discharge Date
- Counting patients
- Average, Maximum, Minimum
- Database information

Category 2: RAG
Use RAG when the question is about:
- Hospital policies
- Leave policy
- Privacy policy
- Infection control
- Emergency procedures
- Visitor policy
- Staff guidelines
- Hospital rules
- Code Blue
- PPE
- Confidentiality

Return ONLY one word.

SQL

or

RAG

User Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content.strip().upper()


def orchestrate(question):
    """
    Route the question to the correct AI agent.
    """

    agent = classify_query(question)

    # ---------- SQL AGENT ----------
    if agent == "SQL":

        sql, result = ask_database(question)

        # If database returns an error
        if result is None:
            return "Sorry, I couldn't retrieve the requested information."

        # Return DataFrame directly to Streamlit
        return result

    # ---------- RAG AGENT ----------
    elif agent == "RAG":

        return ask_ai(question)

    # ---------- FALLBACK ----------
    else:

        return "Sorry, I couldn't determine how to answer your question."