from flask import Blueprint, render_template
import requests

website_bp = Blueprint('website', __name__)

@website_bp.app_context_processor
def data():
    genres_response = requests.get('http://127.0.0.1:5000/genres')
    genres = genres_response.json()
    
    studio_response = requests.get('http://127.0.0.1:5000/studios')
    studios = studio_response.json()
    
    anime_response = requests.get('http://127.0.0.1:5000/anime')
    animes = anime_response.json()
    
    return dict(global_genres=genres, global_studios = studios, global_animes = animes)


@website_bp.route('/')
def index():
    return render_template('website/index.html')

@website_bp.route('/anime-detail/<int:id>')
def animeDetail(id):
    anime_response = requests.get(f'http://127.0.0.1:5000/anime/{id}')
    anime = anime_response.json()
    
    return render_template('website/detail.html',anime=anime)


@website_bp.route('/enime-categories')
def categories():
    return render_template('website/categories.html')

@website_bp.route('/enime-categories/<int:id>')
def animeCategory(id):
    genres_response = requests.get('http://127.0.0.1:5000/genres')
    genres = genres_response.json()
    
    anime_response = requests.get('http://127.0.0.1:5000/anime')
    animes = anime_response.json()
    
    selected_genre = next((genre for genre in genres if genre['id'] == id), None)
    
    if not selected_genre:
        return render_template('website/anime-category.html', genres=genres, animes=[], selected_genre=None)
    
    filtered_animes = [anime for anime in animes if selected_genre['name'] in anime['genres']]
    
    return render_template('website/anime-category.html', genres=genres, animes=filtered_animes, selected_genre=selected_genre)

@website_bp.route('/enime-top')
def topAnime():
    anime_response = requests.get('http://127.0.0.1:5000/anime')
    animes = anime_response.json()
    
    top_animes = [anime for anime in animes if anime['rating'] > 8]
    
    return render_template('website/top-anime.html', animes=top_animes)

