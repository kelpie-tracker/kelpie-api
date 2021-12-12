from flask import request, Blueprint, jsonify

# Depencias do projeto
from models.position import *
from models.fence import *
from models.base import db, ma
from groups.consumer import *

kelpie_routes = Blueprint('index', __name__)

@kelpie_routes.route("/")
def home():
    return "Hello World!"

@kelpie_routes.route("/healthcheck", methods=['GET'])
def healthcheck():
    '''
    Application Healtcheck
    '''
    return "WORKING"

@kelpie_routes.route('/positions', methods=['GET','POST'])
def positions():
    if request.method == "POST":
        content = request.json
        new_position = Position(content['id'], content['longitude'], content['latitude'])
        db.session.add(new_position)
        db.session.commit()
        return jsonify({"message": "new position added"})
    return jsonify(positions_schema.dump(get_positions()))

@kelpie_routes.route('/fences', methods=['GET','POST'])
def fences():
    if request.method == "POST":
        content = request.json
        new_position = Fence(content['up'], content['bottom'], content['right'], content['left'])
        db.session.add(new_position)
        db.session.commit()
        return jsonify({"message": "new fence added"})
    return jsonify(fences_schema.dump(get_fences()))
