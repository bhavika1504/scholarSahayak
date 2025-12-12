# models/scholarship_model.py
from models.db_connection import get_db_connection
import datetime

class ScholarshipModel:

    @staticmethod
    def get_all_scholarships():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM scholarships ORDER BY created_at DESC")
        data = cursor.fetchall()
        conn.close()
        return data or []

    @staticmethod
    def get_scholarship_by_id(scholarship_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM scholarships WHERE scholarship_id = %s", (scholarship_id,))
        s = cursor.fetchone()
        conn.close()
        return s

    @staticmethod
    def get_eligibility_for_scholarship(scholarship_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM eligibility_criteria WHERE scholarship_id = %s", (scholarship_id,))
        crit = cursor.fetchone()
        conn.close()
        return crit

    @staticmethod
    def get_all_with_eligibility():
        """
        Returns list of scholarships joined with their eligibility criteria (if any)
        """
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
        SELECT s.*, e.criteria_id, e.income_limit, e.category_required, e.course_required,
               e.education_required, e.min_marks, e.gender
        FROM scholarships s
        LEFT JOIN eligibility_criteria e ON s.scholarship_id = e.scholarship_id
        ORDER BY s.created_at DESC
        """
        cursor.execute(query)
        rows = cursor.fetchall() or []
        conn.close()
        return rows

    @staticmethod
    def apply(student_id, scholarship_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM applications_tracked WHERE student_id=%s AND scholarship_id=%s",
                       (student_id, scholarship_id))
        if cursor.fetchone():
            conn.close()
            return {"status": False, "message": "Already applied"}

        cursor.execute("INSERT INTO applications_tracked (student_id, scholarship_id, status, created_at) VALUES (%s, %s, %s, NOW())",
                       (student_id, scholarship_id, 'Applied'))
        conn.commit()
        conn.close()
        return {"status": True, "message": "Application submitted"}

    @staticmethod
    def get_applications(student_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT a.track_id, a.status, a.created_at AS applied_at,
                   s.scholarship_id, s.title, s.amount, s.provider_type
            FROM applications_tracked a
            JOIN scholarships s ON a.scholarship_id = s.scholarship_id
            WHERE a.student_id = %s
            ORDER BY a.created_at DESC
        """, (student_id,))
        rows = cursor.fetchall() or []
        conn.close()
        return rows
