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

    @staticmethod
    def get_student_by_id(student_id):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM students WHERE student_id = %s"
            cursor.execute(query, (student_id,))
            return cursor.fetchone()
        except Exception as e:
            print("❌ ERROR (get_student_by_id):", e)
            return None
        finally:
            if conn:
                conn.close()

    @staticmethod
    def update_student(student_id, updates: dict):
        """
        updates: dict of columns to update, e.g.
        {"phone": "9999", "education_level": "UG", "password": "<raw password (will be hashed)>"}
        Returns True on success, False or raises exception on failure.
        """
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # allowed fields to update
            allowed = {"name", "phone", "education_level", "course",
                       "category", "annual_income", "state_id", "email", "password"}

            # filter updates
            data = {k: v for k, v in updates.items() if k in allowed and v is not None}

            if not data:
                return {"status": False, "message": "No valid fields to update."}

            # handle password hashing if present
            if "password" in data:
                data["password"] = generate_password_hash(data["password"])

            # build query dynamically
            set_clause = ", ".join(f"{k} = %s" for k in data.keys())
            values = list(data.values())
            values.append(student_id)  # for WHERE

            sql = f"UPDATE students SET {set_clause} WHERE student_id = %s"
            cursor.execute(sql, tuple(values))
            conn.commit()

            return {"status": True, "message": "Profile updated successfully."}

        except Exception as e:
            print("❌ ERROR (update_student):", e)
            return {"status": False, "message": str(e)}
        finally:
            if conn:
                conn.close()
