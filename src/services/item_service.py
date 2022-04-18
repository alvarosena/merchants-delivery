from this import d
from models import db, Item, Category, item_schema, items_schema

class ItemService:
    def create_item(self, data, category_id):
        category_exists = Category.query.filter_by(id=category_id).first()
        item_exists = Item.query.filter_by(name=data['name']).first()

        if not category_exists:
            raise Exception('Category not found.')
        elif item_exists:
            raise Exception('Item already exists.')
        else:
            item = Item(
                photo_url=data['photo_url'],
                name=data['name'], 
                description=data['description'],
                price=data['price'],
                category_id=category_exists.id
            )

            db.session.add(item)
            db.session.commit()

            return item_schema.dump(item)

    def list_items(self):
        items = Item.query.all()
        return items_schema.dump(items)    

    def delete_item(self, item_id):
        item = Item.query.filter_by(id=item_id).first()

        if not item:
            raise Exception("Item does not exists.")
        else:
            db.session.delete(item)
            db.session.commit()
