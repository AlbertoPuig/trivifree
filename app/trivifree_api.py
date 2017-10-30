from flask import Flask, request, make_response, abort
from flask_restful import Resource, Api
from json import dumps
from flask.ext.jsonpify import jsonify
import json
import logging

app = Flask(__name__)
api = Api(app)

class Quest(Resource):
    def get(self, question_id):
       

        result = ''
        logging.basicConfig(filename='file.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
        logging.debug('Init')
        #encoded
        data_string = json.dumps(result)
        #Decoded
        decoded = json.loads(data_string)
        #return 'Employees_Name'
        if question_id.isdigit():
            question = 'Q'
            question += question_id
            try:
                with open('data.json', 'r') as f:
                    data = json.load(f)
                    try:
                        question_data = data[question]
                        logging.debug('Response for params: ' + question_id)
                        return make_response(jsonify(question_data),200)       
                    except Exception as ex:
                        print ("Not found. Param error")
                        return make_response(jsonify(),500)
            except Exception as e:
                #message to log
                print (e)
                #return error
                return make_response(jsonify(e),500) 
        else:
            return abort(400)


api.add_resource(Quest, '/trivifree/api/v1/quest/<question_id>') # Route_3


if __name__ == '__main__':
       app.run(host='127.0.0.1', port=8080)