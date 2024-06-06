from flask import Flask
from config import create_app
from controllers.anime_controller import anime_bp
from controllers.genre_controller import genre_bp
from controllers.studio_controller import studio_bp

app = create_app()

app.register_blueprint(anime_bp, url_prefix='/')
app.register_blueprint(genre_bp, url_prefix='/')
app.register_blueprint(studio_bp, url_prefix='/')

