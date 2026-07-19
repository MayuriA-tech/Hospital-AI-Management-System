from database.hospital_database import execute_query


def get_dashboard_data():

    data = {}

    # Total Patients
    df = execute_query("SELECT COUNT(*) AS total FROM patients")
    data["patients"] = int(df.iloc[0]["total"])

    # Total Hospitals
    df = execute_query(
        "SELECT COUNT(DISTINCT Hospital) AS total FROM patients"
    )
    data["hospitals"] = int(df.iloc[0]["total"])

    # Total Doctors
    df = execute_query(
        "SELECT COUNT(DISTINCT Doctor) AS total FROM patients"
    )
    data["doctors"] = int(df.iloc[0]["total"])

    # Average Billing
    df = execute_query(
        "SELECT AVG([Billing Amount]) AS avg_bill FROM patients"
    )

    data["billing"] = round(float(df.iloc[0]["avg_bill"]), 2)

    return data


def get_full_dataset():

    return execute_query(
        """
        SELECT *
        FROM patients
        """
    )


def get_recent_patients():

    return execute_query(
        """
        SELECT
            Name,
            Age,
            Gender,
            Doctor,
            Hospital,
            [Medical Condition]
        FROM patients
        LIMIT 10
        """
    )