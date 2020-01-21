
import pymongo
from flask import request
from flask import jsonify
from bson.json_util import dumps
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

client = pymongo.MongoClient("mongodb+srv://user01:bl4ck4dd3r@cluster0-kooqx.mongodb.net/test?retryWrites=true&w=majority")
db = client.sample_airbnb
collection = db.listingsAndReviews


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/name/', methods=['GET'])
def api_all():
    name = request.args.get('name')
    result = collection.find({"name":name})
    return jsonify(dumps(result))


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


app.run()
