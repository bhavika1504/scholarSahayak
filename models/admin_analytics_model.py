from models.db_connection import get_db_connection

class AnalyticsModel:

    @staticmethod
    def total_students():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM students")
        count = cursor.fetchone()[0]
        conn.close()
        return count

    @staticmethod
    def total_scholarships():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM scholarships")
        count = cursor.fetchone()[0]
        conn.close()
        return count

    @staticmethod
    def total_applications():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM applied_scholarships")
        count = cursor.fetchone()[0]
        conn.close()
        return count
