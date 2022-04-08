from models import db, Merchant
from werkzeug.security import generate_password_hash

class MerchantService:
    def create_merchant(self, data):
        merchant_exists = Merchant.query.filter_by(name=data['name']).first()

        if merchant_exists:
            raise Exception('Merchant already exists!')
        else:
            hashedPassword = generate_password_hash(data['password'])
            
            merchant = Merchant(
                photo_url=data['photo_url'], 
                name=data['name'],
                email=data['email'], 
                password=hashedPassword
            )

            db.session.add(merchant)
            db.session.commit()

            result = {
                'id': merchant.id,
                'photo_url': merchant.photo_url,
                'name': merchant.name,
                'email': merchant.email,
            }

            return result