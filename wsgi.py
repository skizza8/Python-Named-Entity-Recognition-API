import os
from flask import Flask, jsonify, request, json, Blueprint
from flask_restx import Api, Resource, reqparse
import requests
import traceback
import logger
from NER_Model import NER_Model
from werkzeug.exceptions import HTTPException
from flask_cors import CORS

#api_bp = Blueprint("api", __name__, url_prefix="/api/test/v1")
app = Flask(__name__)
CORS(app)
# app.register_blueprint(api_bp)
api = Api(
    app
)

ner_model = NER_Model()

@api.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "response_code": e.code,
        "content": e.name,
        "response_message": e.description,
    })
    response.content_type = "application/json"
    return response

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):

        try:

            return ({'response_code': 'Msg', 'response_message': '%s' % ('Welcome to NER API')}), 200

        except Exception as ex:
            #raise ex
            return ({'response_code': 'Err', 'response_message': '%s' % (ex)}), 400


@api.route('/ner')
class get_ner(Resource):
    def post(self):

        try:
            parser = reqparse.RequestParser()
            parser.add_argument('sentence', type=str,
                                help='Add a Sentence', default='Hello, World!')
            
            args = parser.parse_args()

            sentence = args['sentence']
            
            retvalue = ner_model.get_ner(sentence)
            
            return ({'response_code': 'Msg', 'response_message': '%s' % (retvalue)}), 200
        except Exception as ex:
            logger.log_message(traceback.print_exc())
            #raise ex
            return ({'response_code': 'Err', 'response_message': '%s' % (ex)}), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2020, debug=True)