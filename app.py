from flask import Flask
from routes.auth_routes import auth
from routes.student_routes import student_bp   # <-- import the new blueprint
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

CORS(app)

# register blueprints
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(student_bp, url_prefix="/student")  # <-- new

@app.route("/")
def home():
    return {"message": "Scholarship AI System Running"}

if __name__ == "__main__":
    app.run(debug=True)
