from flask import Blueprint, jsonify, request
from services.category_service import CategoryService
from flask_jwt_extended import jwt_required, get_jwt_identity

categories = Blueprint('categories', __name__)

@categories.route('/categories', methods=['POST'])
@jwt_required()
def create_category():
    try:
        current_merchant = get_jwt_identity()
        categoryService = CategoryService()

        data = request.json
        category = categoryService.create_category(data, current_merchant)

        return jsonify(category), 201
    except Exception as err:
        return jsonify({'error': str(err)}), 400

@categories.route('/categories')
def list_categories():
    try:
        categoryService = CategoryService()

        categories = categoryService.list_categories()
        return jsonify(categories)
    except Exception as err:
        return jsonify({'error': str(err)}), 400

@categories.route('/categories/<category_id>/delete', methods=["DELETE"])
def delete_category(category_id):
    try:
        categoryService = CategoryService()

        categoryService.delete_category(category_id)
        return jsonify(), 204
    except Exception as err:
        return jsonify({'error': str(err)}), 404