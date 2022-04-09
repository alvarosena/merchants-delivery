from models import db, Category, Merchant, category_schema

class CategoryService:
    def create_category(self, data, current_merchant):
        merchant_exists = Merchant.query.filter_by(id=current_merchant).first()
        category_exists = Category.query.filter_by(name=data['name']).first()

        if not merchant_exists:
            raise Exception('Merchant not found.')
        elif category_exists:
            raise Exception('Category already exists.')
        else:
            category = Category(name=data['name'],  merchant_id=merchant_exists.id)
            db.session.add(category)
            db.session.commit()

            return category_schema.dump(category)
