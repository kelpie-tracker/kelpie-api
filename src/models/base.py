from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


## Declarative base
# from sqlalchemy.ext.declarative import declarative_base
# from flask_marshmallow import Marshmallow
# Base = declarative_base()
# ma = Marshmallow()

db = SQLAlchemy()
ma = Marshmallow()
