#!/usr/bin/python3
"""Main route"""

from api.v1.views import app_views
from flask import Flask
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {
    "amenities": Amenity,
    "cities": City,
    "places": Place,
    "reviews": Review,
    "states": State,
    "users": User
}


@app_views.route('/status')
def status_check():
    """
    checks the status of JSON
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    '''
    retrieves the number of each objects by type
    '''
    obj_count = {}
    for key, value in classes.items():
        obj_count[key] = storage.count(value)
    return jsonify(obj_count)


if __name__ == '__main__':
    pass
