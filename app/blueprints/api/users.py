from .import bp as api
from flask import jsonify

@api.route('/')

def get_users():
    """
    [GET]/api/users
    """
    #jsonify only takess a list of dictionaries/a sing dictonary 
    return jsonify({'message': 'This works'})
