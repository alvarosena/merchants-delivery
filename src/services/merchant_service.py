from models import db, Merchant, merchants_schema
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

class MerchantService:
    def create_merchant(self, data):
        merchant_exists = Merchant.query.filter_by(name=data['name']).first()

        if merchant_exists:
            raise Exception('Merchant already exists!')
        else:
            hashed_password = generate_password_hash(data['password'])
            
            merchant = Merchant(
                photo_url=data['photo_url'], 
                name=data['name'],
                email=data['email'], 
                password=hashed_password
            )

            db.session.add(merchant)
            db.session.commit()

            result = {
                'id': merchant.id,
                'photo_url': merchant.photo_url,
                'name': merchant.name,
                'email': merchant.email,
                'created_at': merchant.created_at
            }

            return result

    def authenticate_merchant(self, data):
        merchant = Merchant.query.filter_by(email=data['email']).first()

        password_match = check_password_hash(merchant.password, data['password'])

        if not password_match:
            raise Exception("Password don't match!")
        else:
            access_token = create_access_token(identity=merchant.id)

            result = {
                'access_token': access_token
            }

            return result

    def list_all_merchants(self):
        merchants = Merchant.query.all()
        
        return merchants_schema.dump(merchants)