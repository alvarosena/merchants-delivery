from models import db, Merchant

class MerchantService:
    def create_merchant(self, data):
        merchant_exists = Merchant.query.filter_by(name=data['name']).first()

        if merchant_exists:
            raise Exception('Merchant already exists!')
        else:
            merchant = Merchant(photo_url=data['photo_url'], name=data['name'])

            db.session.add(merchant)
            db.session.commit()

            result = {
                'id': merchant.id,
                'photo_url': merchant.photo_url,
                'name': merchant.name
            }

            return result