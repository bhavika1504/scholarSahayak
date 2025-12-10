import jwt
import datetime
from werkzeug.security import check_password_hash
from models.student_model import StudentModel

SECRET_KEY = "71eb1bb6db1716f62940c9c867ea1bdc0ce1d16c62a1fa60b6896f6a08868eda"

class AuthController:

    @staticmethod
    def login(data):
        try:
            email = data.get("email")
            password = data.get("password")

            # 1. Check if student exists
            student = StudentModel.get_student_by_email(email)

            if not student:
                return {"message": "Email not registered", "status": False}

            # 2. Verify password
            if not check_password_hash(student["password"], password):
                return {"message": "Incorrect password", "status": False}

            # 3. Create JWT token
            token = jwt.encode(
                {
                    "id": student["id"],
                    "email": student["email"],
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=10)
                },
                SECRET_KEY,
                algorithm="HS256"
            )

            # 4. Return success response
            return {
                "message": "Login successful",
                "status": True,
                "token": token,
                "student": {
                    "id": student["id"],
                    "name": student["name"],
                    "email": student["email"]
                }
            }

        except Exception as e:
            print("❌ ERROR (login):", e)
            return {"message": "Login failed", "status": False}
