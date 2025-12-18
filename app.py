# app.py (snippet)
from flask import Flask
from routes.auth_routes import auth
from routes.student_routes import student_bp   # add this import
from flask_cors import CORS
from routes.scholarship_routes import scholarship_bp
from routes.admin_routes import admin_bp


app = Flask(__name__)
CORS(app)

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(student_bp, url_prefix="/student")
app.register_blueprint(scholarship_bp, url_prefix="/scholarships")
app.register_blueprint(admin_bp, url_prefix="/admin")


@app.route("/")
def home():
    return {"message": "Scholarship AI System Running"}

if __name__ == "__main__":
    app.run(debug=True)
