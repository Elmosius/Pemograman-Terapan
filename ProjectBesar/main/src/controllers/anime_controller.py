from flask import Blueprint, request, jsonify
from services.anime_service import create_anime, get_all_animes, get_anime_by_id, update_anime, delete_anime

anime_bp = Blueprint('anime_bp', __name__)

@anime_bp.route('/anime', methods=['POST'])
def add_anime():
    data = request.get_json()
    anime = create_anime(data)
    genres = [genre.name for genre in anime.genres]  
    anime_dict = {
        "id": anime.id,
        "title": anime.title,
        "author": anime.author,
        "image": anime.image,
        "episodes": anime.episodes,
        "synopsis": anime.synopsis,
        "season": anime.season,
        "status": anime.status,
        "rating": anime.rating,
        "genres": genres,  
        "studio_id": anime.studio_id
    }
    return jsonify({'message': 'Anime added successfully!', 'anime': anime_dict}), 201


@anime_bp.route('/anime', methods=['GET'])
def get_animes():
    animes = get_all_animes()
    results = []
    for anime in animes:
        genres = [genre.name for genre in anime.genres]
        result = {
            "id": anime.id,
            "title": anime.title,
            "author": anime.author,
            "image": anime.image,
            "episodes": anime.episodes,
            "synopsis": anime.synopsis,
            "season": anime.season,
            "status": anime.status,
            "rating": anime.rating,
            "genres": genres,
            "studio": anime.studio.name
        }
        results.append(result)
    return jsonify(results), 200

@anime_bp.route('/anime/<int:id>', methods=['GET'])
def get_anime(id):
    anime = get_anime_by_id(id)
    genres = [genre.name for genre in anime.genres]
    result = {
        "id": anime.id,
        "title": anime.title,
        "author": anime.author,
        "image": anime.image,
        "episodes": anime.episodes,
        "synopsis": anime.synopsis,
        "season": anime.season,
        "status": anime.status,
        "rating": anime.rating,
        "genres": genres,
        "studio": anime.studio.name
    }
    return jsonify(result), 200

@anime_bp.route('/anime/<int:id>', methods=['PUT'])
def update_anime_endpoint(id):
    data = request.get_json()
    anime = update_anime(id, data)
    genres = [genre.name for genre in anime.genres] 
    anime_dict = {
        "id": anime.id,
        "title": anime.title,
        "author": anime.author,
        "image": anime.image,
        "episodes": anime.episodes,
        "synopsis": anime.synopsis,
        "season": anime.season,
        "status": anime.status,
        "rating": anime.rating,
        "genres": genres,  
        "studio_id": anime.studio_id
    }
    return jsonify({'message': 'Anime updated successfully!', 'anime': anime_dict}), 200


@anime_bp.route('/anime/<int:id>', methods=['DELETE'])
def delete_anime_endpoint(id):
    anime = delete_anime(id)
    return jsonify({'message': 'Anime deleted successfully!', 'anime_id': anime.id}), 200
