from models.base import db, ma
import datetime

class Position(db.Model):
    __tablename__ = 'positions'
    id = db.Column(db.String(255), primary_key=True)
    date = db.Column(db.DateTime(), default=datetime.datetime.now())
    longitude = db.Column(db.Float(24))
    latitude = db.Column(db.Float(24))

    def __init__(self, id, longitude, latitude):
        self.id = id
        self.date = datetime.datetime.now()
        self.longitude = longitude
        self.latitude = latitude

# Position Schema
class PositionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'longitude', 'latitude')

positions_schema = PositionSchema(many=True)