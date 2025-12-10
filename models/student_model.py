from werkzeug.security import generate_password_hash
from models.db_connection import get_db_connection


class StudentModel:

    @staticmethod
    def create_student(data):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO students 
                (name, email, password, phone, state_id, category, annual_income, 
                 education_level, course, created_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
            """

            hashed_password = generate_password_hash(data["password"])

            values = (
                data["name"],
                data["email"],
                hashed_password,
                data["phone"],
                data["state_id"],
                data["category"],
                data["annual_income"],
                data["education_level"],
                data["course"]
            )

            cursor.execute(query, values)
            conn.commit()

            return {"message": "Student registered successfully!", "status": True}

        except Exception as e:
            print("❌ ERROR (create_student):", e)
            return {"message": "Registration failed", "error": str(e), "status": False}

        finally:
            if conn:
                conn.close()

    # ---------------------------------------------------------

    @staticmethod
    def get_student_by_email(email):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            query = "SELECT * FROM students WHERE email = %s"
            cursor.execute(query, (email,))
            return cursor.fetchone()

        except Exception as e:
            print("❌ ERROR (get_student_by_email):", e)
            return None

        finally:
            if conn:
                conn.close()
