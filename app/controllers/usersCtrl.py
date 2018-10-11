from app import app
from app.dal.dal import get_dal
from app.config.config import usersCollName
from bson.json_util import dumps
from flask import request, jsonify
import json
import ast
import imp


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