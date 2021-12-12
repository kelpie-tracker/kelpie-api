import os
## CONF MYSQL
MYSQL_ENDPOINT = os.environ.get('MYSQL_ENDPOINT', 'mysql://root:MySql2019!@db/testedb')
# Aumentar a persistência da conexão ao banco
SQLALCHEMY_POOL_RECYCLE = 280
SQLALCHEMY_POOL_TIMEOUT = 20
SQLALCHEMY_POOL_PRE_PING = True
# Bug com conector "mysql" no python3 por isso foi usado mysqlconnector
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}'.format(MYSQL_ENDPOINT[8:])
## CONF FLASK
SECRET_KEY = os.urandom(24)
## LOCAL
basedir = os.path.abspath(os.path.dirname(__file__))
# Ajuste dos ambientes
ENV = os.environ.get('ENV','prod')
if ENV == "prod":
    LEVEL='INFO'
    DEBUG=False
else:
    LEVEL='DEBUG'
    DEBUG=True