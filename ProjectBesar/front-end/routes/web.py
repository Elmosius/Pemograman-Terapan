from flask import Blueprint, render_template
import requests

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def index():
    studio_response = requests.get('http://127.0.0.1:5000/studios')
    studios = studio_response.json()

    genres_response = requests.get('http://127.0.0.1:5000/genres')
    genres = genres_response.json()
    
    anime_response = requests.get('http://127.0.0.1:5000/anime')
    anime = anime_response.json()
    
    return render_template('dashboard/index.html', studios=studios,genres=genres,anime=anime)
