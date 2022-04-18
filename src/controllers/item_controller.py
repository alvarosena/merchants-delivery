from flask import Blueprint, jsonify, request
from services.item_service import ItemService
from flask_jwt_extended import jwt_required

items = Blueprint('items', __name__)

@items.route('/items/<category_id>', methods=['POST'])
def create_item(category_id):
    try:
        itemService = ItemService()

        data = request.json

        item = itemService.create_item(data, category_id)   
        return jsonify(item), 201
    except Exception as err:
        return jsonify({'error': str(err)}), 400

@items.route('/items')
def list_items():
    try:
        itemService = ItemService()

        items = itemService.list_items()

        return jsonify(items)
    except Exception as err:
        return jsonify({'error': str(err)}), 400

@items.route('/items/<item_id>/delete', methods=["DELETE"])
def delete_item(item_id):
    try:
        itemService = ItemService()
        itemService.delete_item(item_id)
        return jsonify(), 204
    except Exception as err:
        return jsonify({'error': str(err)}), 404