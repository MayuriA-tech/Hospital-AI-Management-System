def validate_sql(sql):
    """
    Allows only safe SELECT queries.
    """

    sql = sql.strip().lower()

    # Query must start with SELECT
    if not sql.startswith("select"):
        return False

    # Block dangerous SQL commands
    blocked_keywords = [
        "drop",
        "delete",
        "update",
        "insert",
        "alter",
        "truncate",
        "create",
        "replace",
        "grant",
        "revoke"
    ]

    for keyword in blocked_keywords:
        if keyword in sql:
            return False

    return True