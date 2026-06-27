from app.database import get_db_connection


def log_action(user_id, action):

    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO audit_logs
        (
            user_id,
            action
        )
        VALUES
        (
            %s,
            %s
        )
        """,
        (user_id, action)
    )

    connection.commit()

    cursor.close()
    connection.close()