from app import app
from flask import jsonify, render_template, request
import app.controllers.usersCtrl as uCtrl
import json
import ast
import imp
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

def parse_query_params(query_string):
    query_params = dict(urlparse.parse_qs(query_string))
    query_params = {k: v[0] for k, v in query_params.items()}
    return query_params

# Root
@app.route("/")
def root_response():
    message = {
        'status': '200',
        'message': 'Welcome to the Python Rest API',
        'apiVersion': 'Version 1.0',
        'by': 'Miguel Pimenta'
    }
    return render_template('index.html', message=message)

# Create User
@app.route("/users", methods=['POST'])
def create_user():
    try:
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except Exception as e:
            message = {
                'status': '400',
                'message': 'Bad request.',
                'error': str(e)
            }
            return jsonify(message), 400
        # Controller
        return (uCtrl.create_user(body))
    except Exception as e:
        message = {
            'status': '500',
            'message': 'Sorry, an error occurred',
            'error': str(e)
        }
        return jsonify(message), 500


def create_user():
    message = {
        'status': '501',
        'message': 'Create User Not implemented.',
    }
    return jsonify(message), 501

# Read User
@app.route("/users/<user_id>", methods=['GET'])
def read_user(user_id):
    message = {
        'status': '501',
        'message': 'Read User Not implemented.',
    }
    return jsonify(message), 501

# Update User
@app.route("/users/<user_id>", methods=['POST'])
def update_user(user_id):
    message = {
        'status': '501',
        'message': 'Update User Not implemented.',
    }
    return jsonify(message), 501

# Delete Record
@app.route("/users/<user_id>", methods=['DELETE'])
def remove_user(user_id):
    message = {
        'status': '501',
        'message': 'Delete Record Not implemented.',
    }
    return jsonify(message), 501

# List Users
@app.route("/users", methods=['GET'])
def list_search_users():
    message = {
        'status': '501',
        'message': 'List/Search Users Not implemented.',
    }
    return jsonify(message), 501


@app.errorhandler(400)
def bad_request(e):
    print(str(e))
    message = {
        'status': '400',
        'message': 'Bad request.',
    }
    return jsonify(message), 400

@app.errorhandler(404)
def page_not_found(e):
    print(str(e))
    message = {
        'status': '404',
        'message': 'This route is currently not supported.'
    }
    return jsonify(message), 404

@app.errorhandler(501)
def not_implemented(e):
    print(str(e))
    message = {
        'status': '501',
        'message': 'Internal server error / Not implemented.',
    }
    return jsonify(message), 501