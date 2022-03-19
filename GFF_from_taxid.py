#import required libraries
from flask import Flask
from flask_restful import Resource, Api
import pymongo
import json

#connect to mango db
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["sample_db"]
collection = db["sample_collection"]

#set environment for flask
app = Flask(__name__)
api = Api(app)

#return the taxid list at /taxons
class taxons_data(Resource):
     def get(self):
        print ("\nlist of taxon available:\n")
        for col in collection.distinct("taxid"):
            print(col)

#return the taxon elements at /taxons/<id>
class taxid_data(Resource):
    def get(self,taxid):
            item_count = collection.count_documents({"taxid":str(taxid)})
            if item_count == 0:
                print("\nno result found for taxid %d\n" % (taxid)) 
            else:
               query = collection.find({"taxid":str(taxid)})
               print("\nTaxon related to the taxid %d:\n" % (taxid))
               for col in query:
                   for keys in col.keys():
                       print ('{', keys, ":" , col[keys] , '}')    

#return the gff file at /files/<id>
class file_data(Resource):
    def get(self,id):
        item_count = collection.count_documents({"taxid":str(id)})
        if item_count == 0:
            print("\nno result found for taxid %d\n" % (id)) 
        else:
            for col in collection.find({"taxid":str(id)}):
               print(col["files"][2]["file"])

#set the end points for flask
api.add_resource(taxons_data, '/taxons')
api.add_resource(taxid_data, '/taxons/<int:taxid>')
api.add_resource(file_data, '/files/<int:id>')

#launch flask test
if __name__ == '__main__':
    app.run(debug=True)