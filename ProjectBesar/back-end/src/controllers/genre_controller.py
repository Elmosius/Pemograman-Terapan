from flask import Blueprint, request, jsonify
from services.genre_service import create_genre, get_all_genres, get_genre_by_id, update_genre, delete_genre

genre_bp = Blueprint('genre_bp', __name__)

@genre_bp.route('/genres', methods=['POST'])
def add_genre():
    data = request.get_json()
    genre = create_genre(data)
    return jsonify({'message': 'Genre added successfully!', 'genre': str(genre)}), 201

@genre_bp.route('/genres', methods=['GET'])
def get_genres():
    genres = get_all_genres()
    results = [
        {
            "id": genre.id,
            "name": genre.name
        } for genre in genres]
    return jsonify(results), 200

@genre_bp.route('/genres/<int:id>', methods=['GET'])
def get_genre(id):
    genre = get_genre_by_id(id)
    result = {
        "id": genre.id,
        "name": genre.name
    }
    return jsonify(result), 200

@genre_bp.route('/genres/<int:id>', methods=['PUT'])
def update_genre_endpoint(id):
    data = request.get_json()
    genre = update_genre(id, data)
    return jsonify({'message': 'Genre updated successfully!', 'genre': str(genre)}), 200

@genre_bp.route('/genres/<int:id>', methods=['DELETE'])
def delete_genre_endpoint(id):
    genre = delete_genre(id)
    return jsonify({'message': 'Genre deleted successfully!', 'genre': str(genre)}), 200
