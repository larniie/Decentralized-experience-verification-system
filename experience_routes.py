from ..services.experience_service import ExperienceService

experience_bp = Blueprint('experience', __name__)
experience_service = ExperienceService()

@experience_bp.route('/experience', methods=['POST'])
def create_experience():
    data = request.get_json()
    # Logic to create experience
    return jsonify({'message': 'Experience created'}), 201

@experience_bp.route('/experience/<id>', methods=['GET'])
def get_experience(id):
    # Logic to get experience
    return jsonify({'id': id, 'title': 'Sample Experience'})
=======
from flask import Blueprint, request, jsonify
from ..services.experience_service import ExperienceService

experience_bp = Blueprint('experience', __name__)
experience_service = ExperienceService()

@experience_bp.route('/experience', methods=['POST'])
def create_experience():
    data = request.get_json()
    experience = experience_service.create_experience(data)
    return jsonify({
        'id': experience.id,
        'title': experience.title,
        'description': experience.description
    }), 201

@experience_bp.route('/experience/<id>', methods=['GET'])
def get_experience(id):
    experience = experience_service.get_experience(id)
    if experience:
        return jsonify({
            'id': experience.id,
            'title': experience.title,
            'description': experience.description
        })
    return jsonify({'error': 'Experience not found'}), 404
