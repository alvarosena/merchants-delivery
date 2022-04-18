from controllers.merchant_controller import merchants
from controllers.address_controller import address
from controllers.category_controller import categories
from controllers.item_controller import items

def routes(app):
    app.register_blueprint(merchants, url_prefix='/api/v1')
    app.register_blueprint(address, url_prefix='/api/v1')
    app.register_blueprint(categories, url_prefix='/api/v1')
    app.register_blueprint(items, url_prefix='/api/v1')