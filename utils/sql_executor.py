from database.hospital_database import execute_query
from utils.sql_validator import validate_sql


def execute_sql(sql):
    """
    Validate SQL before executing it.
    """

    if not validate_sql(sql):
        raise Exception("Unsafe SQL Query Detected!")

    result = execute_query(sql)

    return result