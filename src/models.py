from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.sql import func
import uuid

db = SQLAlchemy()
ma = Marshmallow()

def generate_uuid():
    return str(uuid.uuid4())

class Merchant(db.Model):
    __tablename__ = 'merchants'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    photo_url = db.Column(db.String, nullable=False)
    name = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    adresses = db.relationship('Address')
    openinghours = db.relationship('OpenHour')

class MerchantSchema(ma.Schema):
    class Meta:
        fields = ("id", "photo_url", "name", "email", "created_at")

merchant_schema = MerchantSchema()
merchants_schema = MerchantSchema(many=True)

class Address(db.Model):
    __tablename__ = 'adresses'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    street = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    merchant_id = db.Column(db.String, db.ForeignKey('merchants.id'))

class AddressSchema(ma.Schema):
    class Meta:
        fields = ("id", "photo_url", "name", "email", "created_at")

address_schema = AddressSchema()
adresses_schema = AddressSchema(many=True)

class OpenHour(db.Model):
    __tablename__ = 'openinghours'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    start_time = db.Column(db.String, nullable=False)
    end_time = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    merchant_id = db.Column(db.String, db.ForeignKey('merchants.id'))

