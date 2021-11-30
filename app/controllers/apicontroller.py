from flask import Flask
from flask import jsonify
from flask import request
from app import app
from app.models.api import Api


# @app.route('/api', methods=['GET'])
# def api():
#     return jsonify({'message' : 'Hello, World!'})

# @app.route('/api/all', methods=['GET'])
# def getApiAll():
#     api = Api()
#     data = api.getApiAll()
#     return jsonify({'violations' : data})

# @app.route('/api/<string:id>', methods=['GET'])
# def getApiOne(id):
#     api = Api()
#     data = api.getApiOne(id)
#     return jsonify({'violations' : data})

@app.route('/basic_api/entities', methods=['GET', 'POST'])
def entities():
    if request.method == "GET":
        return {
            'message': 'This endpoint should return a list of entities',
            'method': request.method
        }
    if request.method == "POST":
        return {
            'message': 'This endpoint should create an entity',
            'method': request.method,
		'body': request.json
        }

@app.route('/basic_api/entities/<int:entity_id>', methods=['GET', 'PUT', 'DELETE'])
def entity(entity_id):
    if request.method == "GET":
        return {
            'id': entity_id,
            'message': 'This endpoint should return the entity {} details'.format(entity_id),
            'method': request.method
        }
    if request.method == "PUT":
        return {
            'id': entity_id,
            'message': 'This endpoint should update the entity {}'.format(entity_id),
            'method': request.method,
		'body': request.json
        }
    if request.method == "DELETE":
        return {
            'id': entity_id,
            'message': 'This endpoint should delete the entity {}'.format(entity_id),
            'method': request.method
        }

    # GET /entities - get list of entities
    # POST / entities - create an entity
    # GET / entities/<entity_id> - get entity information
    # PUT / entities/<entity_id> - update entity
    # DELETE / entities/<entity_id> - delete entity
