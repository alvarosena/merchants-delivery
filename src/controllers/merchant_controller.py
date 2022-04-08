from flask import Blueprint, jsonify, request
from services.merchant_service import MerchantService

merchants = Blueprint('merchants', __name__)

@merchants.route('/merchants', methods=['POST'])
def create_merchant():
    try:
        merchantService = MerchantService()

        data = request.json

        merchant = merchantService.create_merchant(data)

        return jsonify(merchant), 201
    except Exception as err:
        return jsonify({'error': str(err)}), 400
