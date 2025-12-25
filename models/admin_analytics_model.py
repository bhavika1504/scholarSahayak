from models.db_connection import get_db_connection

class AdminAnalyticsModel:

    @staticmethod
    def most_applied_scholarships(limit=5):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT 
            s.scholarship_id,
            s.title,
            COUNT(a.applied_id) AS total_applications
        FROM applied_scholarships a
        JOIN scholarships s ON a.scholarship_id = s.scholarship_id
        GROUP BY s.scholarship_id
        ORDER BY total_applications DESC
        LIMIT %s
        """

        cursor.execute(query, (limit,))
        data = cursor.fetchall()
        conn.close()
        return data

    @staticmethod
    def applications_by_category():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT 
            st.category,
            COUNT(a.applied_id) AS total
        FROM applied_scholarships a
        JOIN students st ON a.student_id = st.student_id
        GROUP BY st.category
        """

        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data

    @staticmethod
    def applications_by_state():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT 
            st.state_id,
            COUNT(a.applied_id) AS total
        FROM applied_scholarships a
        JOIN students st ON a.student_id = st.student_id
        GROUP BY st.state_id
        """

        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
