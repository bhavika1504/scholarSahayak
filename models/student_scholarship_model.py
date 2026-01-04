from models.db_connection import get_db_connection

class StudentScholarshipModel:

    @staticmethod
    def get_saved(student_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT 
                s.scholarship_id,
                s.title,
                s.description,
                s.amount,
                s.official_link
            FROM student_scholarships ss
            JOIN scholarships s
              ON ss.scholarship_id = s.scholarship_id
            WHERE ss.student_id = %s
              AND ss.status = 'saved'
        """, (student_id,))

        data = cursor.fetchall()
        conn.close()
        return data
