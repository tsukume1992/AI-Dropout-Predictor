from app.database import get_db_connection


def get_dashboard_counts():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    tables = [
        "students",
        "faculty",
        "subjects",
        "courses"
    ]

    counts = {}

    # Get total records for each table
    for table in tables:
        cursor.execute(f"SELECT COUNT(*) AS total FROM {table}")
        counts[table] = cursor.fetchone()["total"]

    # AI Prediction placeholders
    counts["high_risk"] = 0
    counts["medium_risk"] = 0
    counts["low_risk"] = 0

    # Temporary empty Recent Activities
    # We will connect this to audit_logs in Sprint 8
    counts["activities"] = []

    cursor.close()
    connection.close()

    return counts