from datetime import timedelta
import os
from flask import Flask
from models import db, ma
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from routes.routes import routes

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET_KEY')
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
db.init_app(app)
migrate = Migrate(app, db)
ma.init_app(app)
jwt = JWTManager(app)

routes(app)

@app.route('/')
def root():
    return {'message': 'Server is running'}