from app.database import get_db_connection


# ==========================================================
# Get All Students (Search + Pagination)
# ==========================================================

def get_all_students(search="", page=1, per_page=10):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    offset = (page - 1) * per_page

    base_query = """
        FROM students s
        LEFT JOIN courses c
            ON s.course_id = c.course_id
        LEFT JOIN sections sec
            ON s.section_id = sec.section_id
    """

    where_clause = ""
    params = []

    if search:

        where_clause = """
            WHERE
                s.student_number LIKE %s
                OR s.first_name LIKE %s
                OR s.last_name LIKE %s
                OR c.course_code LIKE %s
        """

        keyword = f"%{search}%"
        params = [keyword, keyword, keyword, keyword]

    cursor.execute(
        "SELECT COUNT(*) AS total " + base_query + where_clause,
        params
    )

    total = cursor.fetchone()["total"]

    query = """
        SELECT

            s.student_id,
            s.student_number,

            CONCAT(
                s.last_name,
                ', ',
                s.first_name,
                ' ',
                IFNULL(s.middle_name,'')
            ) AS full_name,

            c.course_code,
            sec.section_name,

            s.year_level,
            s.status

    """ + base_query + where_clause + """

        ORDER BY s.student_number

        LIMIT %s OFFSET %s

    """

    params.extend([per_page, offset])

    cursor.execute(query, params)

    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return students, total


# ==========================================================
# Get Courses
# ==========================================================

def get_courses():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            course_id,
            course_code
        FROM courses
        ORDER BY course_code
    """)

    data = cursor.fetchall()

    cursor.close()
    connection.close()

    return data


# ==========================================================
# Get Sections
# ==========================================================

def get_sections():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            section_id,
            section_name
        FROM sections
        ORDER BY section_name
    """)

    data = cursor.fetchall()

    cursor.close()
    connection.close()

    return data


# ==========================================================
# Check Duplicate Student Number
# ==========================================================

def student_number_exists(student_number, student_id=None):

    connection = get_db_connection()
    cursor = connection.cursor()

    if student_id:

        cursor.execute("""
            SELECT COUNT(*)
            FROM students
            WHERE student_number=%s
            AND student_id<>%s
        """, (student_number, student_id))

    else:

        cursor.execute("""
            SELECT COUNT(*)
            FROM students
            WHERE student_number=%s
        """, (student_number,))

    exists = cursor.fetchone()[0] > 0

    cursor.close()
    connection.close()

    return exists


# ==========================================================
# Check Duplicate Email
# ==========================================================

def email_exists(email, student_id=None):

    if not email:
        return False

    connection = get_db_connection()
    cursor = connection.cursor()

    if student_id:

        cursor.execute("""
            SELECT COUNT(*)
            FROM students
            WHERE email=%s
            AND student_id<>%s
        """, (email, student_id))

    else:

        cursor.execute("""
            SELECT COUNT(*)
            FROM students
            WHERE email=%s
        """, (email,))

    exists = cursor.fetchone()[0] > 0

    cursor.close()
    connection.close()

    return exists


# ==========================================================
# Save Student
# ==========================================================
def save_student(data):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""

        INSERT INTO students
        (
            student_number,
            first_name,
            middle_name,
            last_name,
            sex,
            birthdate,
            email,
            contact_number,
            address,
            course_id,
            section_id,
            year_level,
            status,
            photo
        )

        VALUES
        (
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
        )

    """,

    (

        data["student_number"],
        data["first_name"],
        data["middle_name"],
        data["last_name"],
        data["sex"],
        data["birthdate"],
        data["email"],
        data["contact_number"],
        data["address"],
        data["course_id"],
        data["section_id"],
        data["year_level"],
        data["status"],
        data["photo"]

    ))

    connection.commit()

    cursor.close()
    connection.close()

# ==========================================================
# Get Student By ID
# ==========================================================

def get_student_by_id(student_id):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""

        SELECT

            s.*,

            c.course_code,
            c.course_name,

            sec.section_name

        FROM students s

        LEFT JOIN courses c
            ON s.course_id=c.course_id

        LEFT JOIN sections sec
            ON s.section_id=sec.section_id

        WHERE s.student_id=%s

    """, (student_id,))

    student = cursor.fetchone()

    cursor.close()
    connection.close()

    return student


# ==========================================================
# Update Student
# ==========================================================

def update_student(student_id, data):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""

        UPDATE students

        SET

            student_number=%s,
            first_name=%s,
            middle_name=%s,
            last_name=%s,
            sex=%s,
            birthdate=%s,
            email=%s,
            contact_number=%s,
            address=%s,
            course_id=%s,
            section_id=%s,
            year_level=%s,
            status=%s

        WHERE student_id=%s

    """,

    (

        data["student_number"],
        data["first_name"],
        data["middle_name"],
        data["last_name"],
        data["sex"],
        data["birthdate"],
        data["email"],
        data["contact_number"],
        data["address"],
        data["course_id"],
        data["section_id"],
        data["year_level"],
        data["status"],
        student_id

    ))

    connection.commit()

    cursor.close()
    connection.close()


# ==========================================================
# Delete Student
# ==========================================================

def delete_student_record(student_id):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id=%s",
        (student_id,)
    )

    connection.commit()

    cursor.close()
    connection.close()