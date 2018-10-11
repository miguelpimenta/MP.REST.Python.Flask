from app import app
from flask import jsonify, render_template

def get():
    return ['v1']

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