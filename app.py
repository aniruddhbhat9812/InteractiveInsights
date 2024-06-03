from flask import Flask, Blueprint
from flask_cors import CORS
# from controller import *
import os
# from app import app
from flask import request, jsonify, session
from flask_cors import CORS
from model.campaign_model import InteractiveInsightsDTO
from services.processing_campaign import genAIOutput
import logging


app = Flask(__name__)

CORS(app, resources={r"*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]}})

main_bp = Blueprint("main", __name__)

@app.route("/ping", methods = ['GET'])
def home():
    return "The server responded successfully", 200

app.register_blueprint(main_bp)

logging.basicConfig(level=logging.INFO)

# @app.route('/InteractiveInsights', methods=['POST'])
# def InteractiveInsights_Output():
#     try:
#         body = request.json
#         print("Step1 Successful")
#         if InteractiveInsightsDTO.validatePayload(body):
#             q = InteractiveInsightsDTO.instance_from_flask_body(body)
#             logging.info(q)
#             print(body)
#             result = genAIOutput(body["query"])
#             if 'error' in result:
#                 return jsonify(result), 500
#             return jsonify(result), 200
#     except Exception as e:
#         return jsonify({'error': f'{str(e)}'}), 503
        

if __name__ == "__main__":
    app.run(debug=True)

# from controller import user_controller

