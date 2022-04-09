import os
from flask import Flask
from models import db
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from controllers.merchant_controller import merchants
from controllers.address_controller import address

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET_KEY')
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(merchants, url_prefix='/api/v1')
app.register_blueprint(address, url_prefix='/api/v1')

@app.route('/')
def root():
    return {'message': 'Hello World'}