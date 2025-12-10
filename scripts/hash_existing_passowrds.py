import os
import sys

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from werkzeug.security import generate_password_hash
from models.db_connection import get_db_connection


def convert_existing_passwords():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Fetch all users
        cursor.execute("SELECT student_id, password FROM students")
        users = cursor.fetchall()

        for student_id, old_password in users:
            new_hashed = generate_password_hash(old_password)

            cursor.execute(
                "UPDATE students SET password = %s WHERE student_id = %s",
                (new_hashed, student_id)
            )

        conn.commit()
        print("✅ All passwords successfully converted to secure hashes!")

    except Exception as e:
        print("❌ ERROR:", e)
        
    finally:
        conn.close()


if __name__ == "__main__":
    convert_existing_passwords()
