from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

#inisiasi object app
app = Flask(__name__)

#inisiasi object API
api = Api(app)

#inisiasi object CORS
CORS(app)

#inisiasi data dict
identitas = {}

#membuat class Resource
class ContohResource(Resource):
    #methode GET dan POST
    def get(self):
        #response = {"msg" : "Ini Rest API"}

        return identitas
    
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]

        identitas['nama'] = nama
        identitas['umur'] = umur

        response = {"msg" : "Data berhasil dikirim"}
        return response

#setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

#run program
if __name__ == "__main__":
    app.run(debug=True, port=9000)