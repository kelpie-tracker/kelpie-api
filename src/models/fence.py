from models.base import db, ma
import datetime

class Fence(db.Model):
    __tablename__ = "fences"
    id = db.Column(db.Integer, primary_key=True)
    up = db.Column(db.Float(24))
    right = db.Column(db.Float(24))
    bottom = db.Column(db.Float(24))
    left = db.Column(db.Float(24))
    registered_on = db.Column(db.DateTime(), default=datetime.datetime.now())

    def __init__(self , up, bottom, right, left):
        self.up = up
        self.right = right
        self.bottom = bottom
        self.left = left
        self.registered_on = datetime.datetime.now()

# Host Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'up','right', 'bottom','left','registered_on')

fence_schema = UserSchema()
fences_schema = UserSchema(many=True)
