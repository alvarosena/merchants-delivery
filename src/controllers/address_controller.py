from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.address_service import AddressService

address = Blueprint('address', __name__)

@address.route('/address', methods=['POST'])
@jwt_required()
def create_address():
    try:
        current_merchant = get_jwt_identity()

        addressService = AddressService()
        data = request.json

        address = addressService.create_address(data, current_merchant)

        return jsonify(address), 201
    except Exception as err:
        return jsonify({'error': str(err)}), 401