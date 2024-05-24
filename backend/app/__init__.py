from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    CORS(app)  # Habilitar CORS para todas las rutas

    from app.routes.user_routes import user_routes
    from app.routes.event_routes import event_routes

    app.register_blueprint(user_routes, url_prefix='/api')
    app.register_blueprint(event_routes, url_prefix='/api')

    @app.before_request
    def before_request():
        g.db = db

    @app.teardown_request
    def teardown_request(exception=None):
        db.session.remove()

    return app
