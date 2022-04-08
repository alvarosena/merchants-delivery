import os
from flask import Flask
from models import db

from flask_migrate import Migrate
from controllers.merchant_controller import merchants
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config["JWT_SECRET_KEY"] = os.environ['JWT_SECRET_KEY']
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(merchants, url_prefix='/api/v1')

@app.route('/')
def root():
    return {'message': 'Hello World'}