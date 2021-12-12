# Depencias do banco
from models.position import *
from models.fence import *
from models.base import db, ma

def create_position(entity_id, date, longitude, latitude):
    new_position = Position(entity_id, date, longitude, latitude)
    db.session.add(new_position)
    db.session.commit()

def create_fence(up, bottom, right, left):
    new_fence = Fence(up, bottom, right, left)
    db.session.add(new_fence)
    db.session.commit()

def get_fences():
    return db.session.query(Fence)

def get_positions():
    return db.session.query(Position)