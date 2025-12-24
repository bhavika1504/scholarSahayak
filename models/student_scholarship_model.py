from models.db_connection import get_db_connection

class StudentScholarshipModel:

    @staticmethod
    def save_scholarship(student_id, scholarship_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            query = """
                INSERT INTO student_scholarships (student_id, scholarship_id, status)
                VALUES (%s, %s, 'saved')
            """
            cursor.execute(query, (student_id, scholarship_id))
            conn.commit()
            return {"status": True, "message": "Scholarship saved"}
        except Exception as e:
            return {"status": False, "message": str(e)}
        finally:
            conn.close()

    @staticmethod
    def apply_scholarship(student_id, scholarship_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            query = """
                INSERT INTO student_scholarships (student_id, scholarship_id, status, applied_at)
                VALUES (%s, %s, 'applied', NOW())
                ON DUPLICATE KEY UPDATE
                    status='applied',
                    applied_at=NOW()
            """
            cursor.execute(query, (student_id, scholarship_id))
            conn.commit()
            return {"status": True, "message": "Scholarship applied"}
        except Exception as e:
            return {"status": False, "message": str(e)}
        finally:
            conn.close()
