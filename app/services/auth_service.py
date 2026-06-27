from app.database import get_db_connection


def get_user_by_username(username):

    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username = %s
        """,
        (username,)
    )

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user


def update_last_login(user_id):

    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET last_login = NOW()
        WHERE user_id = %s
        """,
        (user_id,)
    )

    connection.commit()

    cursor.close()
    connection.close()