from models.db_connection import get_db_connection
from datetime import date
from models.db_connection import get_db_connection

class ScholarshipModel:

    @staticmethod
    def create_scholarship(data):
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO scholarships
        (title, provider_type, state_id, amount, deadline,
         category_required, education_required, course_required,
         income_limit, official_link, description, created_at)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())
        """

        values = (
            data.get("title"),
            data.get("provider_type"),
            data.get("state_id"),
            data.get("amount"),
            data.get("deadline"),
            data.get("category_required"),
            data.get("education_required"),
            data.get("course_required"),
            data.get("income_limit"),
            data.get("official_link"),
            data.get("description")
        )

        cursor.execute(query, values)
        conn.commit()
        conn.close()

        return {"status": True, "message": "Scholarship added successfully"}


    @staticmethod
    def update_scholarship(scholarship_id, data):
        conn = get_db_connection()
        cursor = conn.cursor()

        fields = ", ".join(f"{k}=%s" for k in data.keys())
        values = list(data.values())
        values.append(scholarship_id)

        query = f"UPDATE scholarships SET {fields} WHERE scholarship_id=%s"
        cursor.execute(query, tuple(values))
        conn.commit()
        conn.close()

        return {"status": True, "message": "Scholarship updated"}


    @staticmethod
    def delete_scholarship(scholarship_id):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM scholarships WHERE scholarship_id=%s",
            (scholarship_id,)
        )
        conn.commit()
        conn.close()

        return {"status": True, "message": "Scholarship deleted"}


    @staticmethod
    def get_all_scholarships():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM scholarships")
        data = cursor.fetchall()
        conn.close()

        return data

    @staticmethod
    def get_all_active_scholarships():
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            query = """
            SELECT
                scholarship_id,
                title,
                description,
                amount,
                provider_type,
                state_id,
                official_link,
                created_at,
                deadline,
                income_limit,
                category_required,
                course_required,
                education_required
            FROM scholarships
            WHERE deadline IS NULL OR deadline >= %s
            """

            cursor.execute(query, (date.today(),))
            return cursor.fetchall()

        except Exception as e:
            print("❌ ERROR (get_all_active_scholarships):", e)
            return []

        finally:
            if conn:
                conn.close()
