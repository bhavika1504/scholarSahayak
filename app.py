from flask import Flask
from routes.auth_routes import auth
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# register blueprints
app.register_blueprint(auth, url_prefix="/auth")

@app.route("/")
def home():
    return {"message": "Scholarship AI System Running"}

if __name__ == "__main__":
    app.run(debug=True)
