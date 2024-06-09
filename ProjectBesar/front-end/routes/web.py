from flask import Blueprint, render_template
import requests

website_bp = Blueprint('website', __name__)

@website_bp.route('/')
def index():
    studio_response = requests.get('http://127.0.0.1:5000/studios')
    studios = studio_response.json()

    genres_response = requests.get('http://127.0.0.1:5000/genres')
    genres = genres_response.json()
    
    anime_response = requests.get('http://127.0.0.1:5000/anime')
    animes = anime_response.json()
    
    return render_template('website/index.html', studios=studios,genres=genres,animes=animes)

@website_bp.route('/anime-detail/<int:id>')
def anime_detail(id):

    anime_response = requests.get(f'http://127.0.0.1:5000/anime/{id}')
    anime = anime_response.json()
    
    return render_template('website/detail.html',anime=anime)


@website_bp.route('/enime-categories')
def categories():

    genres_response = requests.get('http://127.0.0.1:5000/genres')
    genres = genres_response.json()
    
    anime_response = requests.get('http://127.0.0.1:5000/anime')
    animes = anime_response.json()
    
    return render_template('website/categories.html',genres=genres, animes=animes)

@website_bp.route('/enime-categories/<int:id>')
def animeCategory(id):
    genres_response = requests.get('http://127.0.0.1:5000/genres')
    genres = genres_response.json()
    
    anime_response = requests.get(f'http://127.0.0.1:5000/anime?genre_id={id}')
    animes = anime_response.json()
    
    selected_genre = next((genre for genre in genres if genre['id'] == id), None)
    
    return render_template('website/anime-category.html', genres=genres, animes=animes, selected_genre=selected_genre)
