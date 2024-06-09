from flask import Flask
import os

from routes.dashboard import dashboard_bp
from routes.studio import studio_bp
from routes.category import category_bp
from routes.anime import anime_bp
from routes.web import website_bp

base_dir = os.path.abspath(os.path.dirname(__file__))
templates = os.path.join(base_dir, '..', 'templates')
static = os.path.join(base_dir, '..', 'static')
app = Flask(__name__, template_folder=templates,static_folder=static)  

app.secret_key = os.urandom(24)

app.register_blueprint(dashboard_bp)
app.register_blueprint(studio_bp)
app.register_blueprint(category_bp)
app.register_blueprint(anime_bp)
app.register_blueprint(website_bp)

