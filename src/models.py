from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import uuid

db = SQLAlchemy()

def generate_uuid():
    return str(uuid.uuid4())

class Merchant(db.Model):
    __tablename__ = 'merchants'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    photo_url = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    adresses = db.relationship('Address')
    openinghours = db.relationship('OpenHour')

class Address(db.Model):
    __tablename__ = 'adresses'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    street = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    merchant_id = db.Column(db.String, db.ForeignKey('merchants.id'))

class OpenHour(db.Model):
    __tablename__ = 'openinghours'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    start_time = db.Column(db.String, nullable=False)
    end_time = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    merchant_id = db.Column(db.String, db.ForeignKey('merchants.id'))

