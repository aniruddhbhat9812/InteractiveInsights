from flask import Flask, Blueprint
from flask_cors import CORS



app = Flask(__name__)

CORS(app, resources={r"*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]}})

main_bp = Blueprint("main", __name__)

@main_bp.route("/ping", methods=["GET"])
def homepage():
    return "The server responded successfully", 200

app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run()

from controller import *