# Import required libraries
from flask import Flask, request, Response, json
from pymongo import MongoClient

# initialize flask
app = Flask(__name__)

# class to initialize the mongodb atlas database and collection
class Mongoinit:
    def __init__(self, data):
        # to use mongodb+srv I had to install dnspython library
        self.client = MongoClient("mongodb+srv://<user>:<password>@<cluster_name>.r52hr.mongodb.net/<database>?retryWrites=true&w=majority")
        database = self.client['greendeck']
        # 'records' is the collection on my mongodb atlas database
        self.records = database['task1']
        self.data = data

    # function to create a document in the collection
    def create(self, document):
        # insert one document in the collection
        results = self.records.insert_one(document)
        # return the response
        results = {'Status' : 'Document_Created', 'Document_ID' : str(results.inserted_id)}
        return results

    # function to do a read of the collection
    def read(self):
        # initializing the results list
        results=[]
        cursor = self.records.find()
        # since there are thousands of rows, it's better to use an iterator to save RAM
        cursor_iter = iter(cursor)
        for record in cursor_iter:
            for data in record:
                if data != '_id': # removing document's object ID
                    results.append({data: record[data]})
        return results

    # function to update any document
    def update(self):
        # this filter works as an identifier for a particular document
        _filter = self.data['Filter']
        # 'NewValues' key will contain the new values to be updated
        response = self.records.update_one(_filter, {"$set": self.data['NewValues']})
        # if any updation has been done, return this
        if response.modified_counts >=1:
            results = {'Status': 'Successfully Updated'}
        # if not, return this
        else:
            results = {'Status': 'No Updation done'}
        return results

    # function to delete a document
    def delete(self, data):
        # again, this will identify and pick up that particular document
        _filter = self.data['Filter']
        # delete that document from the collection
        response = self.records.delete_one(_filter)
        # response, if any deletion has happened
        if response.deleted_counts >= 1:
            results = {'Status': 'Successfully Deleted'}
        # reponse, when there wasn't any
        else:
            results = {'Status': 'Not Found'}
        return results

# defining a decorator and a base method to check connection
@app.route('/')
def base():
    return Response(response=json.dumps({"Status":"UP"}), status=200, mimetype='application/json')

# this function will be use to deal with GET requests, or Read queries
@app.route('/mongo', methods=['GET'])
def api_read():
    # parse into json format
   data = request.json
   # make object of the Mongoinit class
   api_obj = Mongoinit(data)
   # call read function
   results = api_obj.read()
   return Response(response=json.dumps(results), status=200, mimetype='application/json')

# function to deal with POST requests or Write queries
@app.route('/mongo', methods=['POST'])
def api_create():
    data = request.json
    api_obj = Mongoinit(data)
    # extract the document details
    document = data['Document']
    # create the document
    results = api_obj.create(document)
    return Response(response=json.dumps(results), status=200, mimetype='application/json')

# functiom to Update any document
@app.route('/mongo',methods=['PUT'])
def api_update():
    data = request.json
    api_obj = Mongoinit(data)
    results = api_obj.update()
    return Response(response=json.dumps(results), status=200, mimetype='application/json')

# function to delete a document
@app.route('/mongo', methods=['DELETE'])
def api_delete():
    data = request.json
    api_obj = Mongoinit(data)
    results = api_obj.delete(data)
    return Response(response=json.dumps(results), status=200, mimetype='application/json')

# driver program, port can be changed accordingly
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5055)
