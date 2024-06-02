from flask import Blueprint, request, jsonify
from services.studio_service import create_studio, get_all_studios, get_studio_by_id, update_studio, delete_studio

studio_bp = Blueprint('studio_bp', __name__)

@studio_bp.route('/studios', methods=['POST'])
def add_studio():
    data = request.get_json()
    studio = create_studio(data)
    return jsonify({'message': 'Studio added successfully!', 'studio': str(studio)}), 201

@studio_bp.route('/studios', methods=['GET'])
def get_studios():
    studios = get_all_studios()
    results = [
        {
            "id": studio.id,
            "name": studio.name
        } for studio in studios]
    return jsonify(results), 200

@studio_bp.route('/studios/<int:id>', methods=['GET'])
def get_studio(id):
    studio = get_studio_by_id(id)
    result = {
        "id": studio.id,
        "name": studio.name
    }
    return jsonify(result), 200

@studio_bp.route('/studios/<int:id>', methods=['PUT'])
def update_studio_endpoint(id):
    data = request.get_json()
    studio = update_studio(id, data)
    return jsonify({'message': 'Studio updated successfully!', 'studio': str(studio)}), 200

@studio_bp.route('/studios/<int:id>', methods=['DELETE'])
def delete_studio_endpoint(id):
    studio = delete_studio(id)
    return jsonify({'message': 'Studio deleted successfully!', 'studio': str(studio)}), 200
