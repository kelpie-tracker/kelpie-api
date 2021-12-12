from flask import Flask
from flask_migrate import Migrate

# Depencias do projeto
import settings
from models.fence import *
from models.base import db
from handler.index import kelpie_routes

# Inicialização da app
def create_app(config=None,environment=None):
    app = Flask(__name__)
    app.register_blueprint(kelpie_routes)
    app.config.from_object('settings')
    db.init_app(app)
    return app

# Instanciando app
app = create_app()

# Habilitando migrate
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=settings.DEBUG)
