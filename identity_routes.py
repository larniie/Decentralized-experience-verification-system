from flask import Blueprint, request, jsonify
from ..services.identity_service import IdentityService

identity_bp = Blueprint('identity', __name__)
identity_service = IdentityService()

@identity_bp.route('/identity', methods=['POST'])
def create_identity():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        identity = identity_service.create_identity(data)
        return jsonify({'id': identity.id, 'name': identity.name}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@identity_bp.route('/identity', methods=['GET'])
def get_identities():
    identities = identity_service.get_all_identities()
    return jsonify([{'id': identity.id, 'name': identity.name} for identity in identities])

@identity_bp.route('/identity/<id>', methods=['GET'])
def get_identity(id):
    identity = identity_service.get_identity(id)
    if identity:
        return jsonify({'id': identity.id, 'name': identity.name})
    return jsonify({'error': 'Identity not found'}), 404
