from models import Merchant, db, Address, address_schema

class AddressService:
    def create_address(self, data, current_merchant):
        merchant_exists = Merchant.query.filter_by(id=current_merchant).first()

        if not merchant_exists:
            raise Exception('Merchant not found.')
        else:
            address = Address(street=data['street'], state=data['state'], merchant_id=merchant_exists.id)
            db.session.add(address)
            db.session.commit()

            return address_schema.dump(address)