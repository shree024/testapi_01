import decimal


import boto3
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from awscli.errorhandler import ClientError
from boto3.dynamodb.conditions import Key
import json
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer
import search_file
from flask_cors import CORS, cross_origin


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)



app = Flask(__name__)
CORS(app)
api = Api(app)

put_args = reqparse.RequestParser()
put_args.add_argument("username", type=str, help="username")
# put_args.add_argument("password",type=str,help="password")

usr = "sumith"
pwd = "Sumi3653"


class Test1(Resource):
    def get(self):
        return {"data": "sumith"}

    def post(self):
        args = put_args.parse_args()
        result = search_file.query_movies1(args["username"])
        # print(type(result))

        if result != False:
            cdf=(json.dumps(result, indent=4, cls=DecimalEncoder))
            cdf= json.loads(cdf)
            return cdf
        else:
            return {"success": "false"}

api.add_resource(Test1, "/api/v1/")

def get_content():
    return "It works!", 200

@app.route('/')
def home():
    content, status_code = get_content()
    headers = {'Access-Control-Allow-Origin': '*'}
    return content, status_code, headers


login_args= reqparse.RequestParser()
login_args.add_argument("username",type=str, help="username")
login_args.add_argument("password",type=str, help="password")

class Login(Resource):
    def post(self):
        log_args=login_args.parse_args()
        result = search_file.login(log_args["username"],log_args["password"])
        return result

api.add_resource(Login,"/api/v1/entry01", methods=['POST', 'GET','OPTIONS'])



CORS(app, support_credentials=True)
@app.route('/api/test', methods=['POST', 'GET','OPTIONS'])
@cross_origin(supports_credentials=True)
def index():
    if(request.method=='POST'):
     some_json=request.get_json()
     print(some_json["username"])
     result = search_file.login(some_json["username"], some_json["password"])
     return jsonify(result)
    else:
        return jsonify({"GET":"GET"})


@app.route('/api/test2', methods=['POST', 'GET','OPTIONS'])
@cross_origin(supports_credentials=True)
def signUp():
    if(request.method=='POST'):
     get_data=request.get_json()

     result = search_file.signUp(get_data["username"], get_data["password"],  get_data["name"], get_data["status"], get_data["phone"],get_data["dob"], get_data["email"],)
     return jsonify(result)
    else:
        return jsonify({"GET":"GET"})

@app.route('/api/test3', methods=['POST', 'GET','OPTIONS'])
@cross_origin(supports_credentials=True)
def addNewBlog():
    if(request.method=='POST'):
     get_data=request.get_json()

     result = search_file.signUp(get_data["name"], get_data["username"],  get_data["place"], get_data["token"], get_data["details"],get_data["image"], get_data["date"],)
     return jsonify(result)
    else:
        return jsonify({"GET":"GET"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
