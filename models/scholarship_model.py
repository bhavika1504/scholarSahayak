from models.db_connection import get_db_connection
from datetime import date

class ScholarshipModel:

    @staticmethod
    def get_all_with_eligibility():
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            query = """
            SELECT 
                s.scholarship_id, s.title, s.description, s.amount,
                s.provider_type, s.state_id, s.official_link,
                s.created_at, s.deadline,
                e.income_limit, e.category_required,
                e.course_required, e.education_required,
                e.min_marks
            FROM scholarships s
            LEFT JOIN eligibility_criteria e 
                ON s.scholarship_id = e.scholarship_id
            WHERE (s.deadline IS NULL OR s.deadline >= %s)
            """

            cursor.execute(query, (date.today(),))
            return cursor.fetchall()

        except Exception as e:
            print("❌ ERROR (get_all_with_eligibility):", e)
            return []

        finally:
            if conn:
                conn.close()
