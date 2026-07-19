import re

from utils.schema_reader import get_schema
from prompts.sql_prompt import build_sql_prompt
from utils.llm_client import get_llm
from utils.sql_executor import execute_sql

llm = get_llm()


def clean_sql(sql):
    """
    Remove markdown formatting from LLM response.
    """

    sql = re.sub(r"```sql", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```", "", sql)

    return sql.strip()


def generate_sql(user_question):
    """
    Generate SQL from natural language.
    """

    schema = get_schema()

    prompt = build_sql_prompt(schema, user_question)

    response = llm.invoke(prompt)

    sql = clean_sql(response.content)

    return sql


def ask_database(user_question):
    """
    Complete NLP → SQL → Database pipeline.
    """

    sql = generate_sql(user_question)

    result = execute_sql(sql)

    return sql, result