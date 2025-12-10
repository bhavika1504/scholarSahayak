import mysql.connector
from werkzeug.security import generate_password_hash
from .db_connection import get_db_connection

class StudentModel:

    @staticmethod
    def create_student(data):
        # Hash the password
        hashed_pw = generate_password_hash(data["password"])

        # Prepare values tuple to match your table columns
        values = (
            data["name"],
            data["email"],
            hashed_pw,
            data["phone"],            # new column you added
            data["state_id"],
            data["category"],
            data["annual_income"]
        )

        # Prepare SQL query
        sql = """
        INSERT INTO students (name, email, password, phone, state_id, category, annual_income)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # Execute query
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
