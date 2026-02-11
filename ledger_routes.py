from flask import Blueprint, request, jsonify
from ..services.blockchain_service import BlockchainService

ledger_bp = Blueprint('ledger', __name__)
blockchain_service = BlockchainService()

@ledger_bp.route('/ledger', methods=['GET'])
def get_ledger():
    # Logic to get ledger data
    return jsonify({'ledger': 'Sample Ledger Data'})

@ledger_bp.route('/ledger/block', methods=['POST'])
def add_block():
    data = request.get_json()
    # Logic to add block to ledger
    return jsonify({'message': 'Block added'}), 201
