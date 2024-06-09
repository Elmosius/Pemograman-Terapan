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



