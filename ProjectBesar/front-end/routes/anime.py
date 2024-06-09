from flask import Blueprint, render_template, redirect, url_for, request, flash
import requests

anime_bp = Blueprint('anime', __name__)

@anime_bp.route('/animes')
def anime():
    response = requests.get('http://127.0.0.1:5000/anime')
    animes = response.json()
    return render_template('animes/index.html', animes=animes)

@anime_bp.route('/animes/<int:id>')
def animeById(id):
    response = requests.get(f'http://127.0.0.1:5000/anime/{id}')
    anime = response.json()
    return render_template('animes/detail.html', anime=anime)

@anime_bp.route('/anime-create', methods=['GET', 'POST'])
def createAnime():
    if request.method == 'POST':
        data = request.form.to_dict(flat=False)  
        response = requests.post('http://127.0.0.1:5000/anime', json=data)  
        if response.status_code == 201:
            flash('Anime created successfully!', 'success')
            return redirect(url_for('anime.anime'))
        else:
            flash('Error creating anime!', 'danger')
            return redirect(url_for('anime.createAnime'))
    else:
        studio_response = requests.get('http://127.0.0.1:5000/studios')
        studios = studio_response.json()

        genres_response = requests.get('http://127.0.0.1:5000/genres')
        genres = genres_response.json()

        statuses = [
            {"value": "completed", "label": "Completed"},
            {"value": "on_progress", "label": "On Progres"}
        ]

        return render_template('animes/create.html', statuses=statuses, studios=studios, genres=genres)

@anime_bp.route('/anime-edit/<int:id>', methods=['GET', 'POST'])
def editAnime(id):
    if request.method == 'GET':
        response = requests.get(f'http://127.0.0.1:5000/anime/{id}')
        anime = response.json()
        
        statuses = [
            {"value": "completed", "label": "Completed"},
            {"value": "on_progress", "label": "On Progres"}
        ]
        
        studio_response = requests.get('http://127.0.0.1:5000/studios')
        studios = studio_response.json()

        genres_response = requests.get('http://127.0.0.1:5000/genres')
        genres = genres_response.json()
        
        return render_template('animes/edit.html', statuses=statuses, studios=studios, genres=genres, anime=anime)
    else:
        data = request.form.to_dict(flat=False)
        response = requests.put(f'http://127.0.0.1:5000/anime/{id}', json=data)
        if response.status_code == 200:
            flash('Anime updated successfully!', 'success')
            return redirect(url_for('anime.anime'))
        else:
            flash('Error updating anime!', 'danger')
            return redirect(url_for('anime.editAnime', id=id))


@anime_bp.route('/anime-delete/<int:id>', methods=['POST'])
def deleteAnime(id):
    response = requests.delete(f'http://127.0.0.1:5000/anime/{id}')
    if response.status_code == 200:
        flash('Anime deleted successfully!', 'success')
    else:
        flash('Error deleting anime!', 'danger')
    return redirect(url_for('anime.anime'))
