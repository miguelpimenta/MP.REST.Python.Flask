from app.dal.dal import get_dal
from app.config.config import usersCollName
from bson.json_util import dumps
from flask import jsonify

# Create User
def create_user(body):
    try:
        dal = get_dal()
        record_created = dal.create(usersCollName, body)
        # Return created Id (or list of Ids)
        if isinstance(record_created, list):
            return jsonify([str(v) for v in record_created]), 201
        else:
            return jsonify(str(record_created)), 201
    except Exception as e:
        message = {
            'status': '500',
            'message': 'Sorry, an error occurred',
            'error': str(e)
        }
        return jsonify(message), 500

# Read User
def read_user(user_id):
    try:
        dal = get_dal()
        user = dal.get_by_id(usersCollName, user_id)
        if user:
            return dumps(user), 200
        else:
            message = {
                'status': '404',
                'message': 'Not found'
            }
            return jsonify(message), 404
    except Exception as e:
        print(str(e))
        message = {
            'status': '500',
            'message': 'Sorry, an error occurred',
        }
        return jsonify(message), 500

# Update User
def update_user(user_id, body):
    try:
        dal = get_dal()
        record_updated = dal.replace(usersCollName, user_id, body)

        # Check if resource is updated and return info
        if record_updated.modified_count == 1:
            message = {
                'status': '200',
                'message': 'Updated with success.'
            }
            return jsonify(message), 200
        else:
            message = {
                'status': '404',
                'message': 'Sorry, record not Found.'
            }
            return jsonify(message), 404
    except Exception as e:
        print(str(e))
        message = {
            'status': '500',
            'message': 'Sorry, an error occurred.'
        }
        return jsonify(message), 500

# Delete Record
def delete_user(user_id):
    try:
        dal = get_dal()
        record_deleted = dal.delete(usersCollName, user_id)
        if record_deleted > 0 :
            message = {
                'status': '200',
                'message': 'Record ' + user_id + ' deleted.'
            }
            return jsonify(message), 200
        else:
            message = {
                'status': '404',
                'message': 'Record ' + user_id + ' not found.'
            }
            return jsonify(message), 404
    except Exception as e:
        print(str(e))
        message = {
            'status': '500',
            'message': 'Sorry, an error occurred'
        }
        return jsonify(message), 500

# List Users
def list_users():
    try:
        dal = get_dal()
        records_fetched = dal.get(usersCollName)
        if len(records_fetched) > 0:
            return dumps(records_fetched)
        else:
            return jsonify([])
    except Exception as e:
        print(str(e))
        message = {
            'status': '500',
            'message': 'Sorry, an error occurred',
        }
        return jsonify(message), 500

# List/Search Users
def search_users(key, value):
    try:
        dal = get_dal()
        records_fetched = dal.find(usersCollName, key, value)
        if records_fetched:
            return dumps(records_fetched), 200
        else:
            message = {
                'status': '404',
                'message': 'Not found'
            }
            return jsonify(message), 404
    except Exception as e:
        print(str(e))
        message = {
            'status': '500',
            'message': 'Sorry, an error occurred',
        }
        return jsonify(message), 500