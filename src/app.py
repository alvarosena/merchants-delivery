import os
from flask import Flask
from models import db

from flask_migrate import Migrate
from controllers.merchant_controller import merchants

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(merchants, url_prefix='/api/v1')

@app.route('/')
def root():
    return {'message': 'Hello World'}