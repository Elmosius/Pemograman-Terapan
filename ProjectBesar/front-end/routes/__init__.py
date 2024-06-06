from flask import Flask, render_template
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
templates = os.path.join(base_dir, '..', 'templates')
static = os.path.join(base_dir, '..', 'static')
app = Flask(__name__, template_folder=templates,static_folder=static)  

@app.route('/')
def index():
    return render_template('/dashboard/index.html')

# studio
@app.route('/studios')
def studios():
    return render_template('/studios/index.html')

@app.route('/studio-create')
def createStudio():
    return render_template('studios/create.html')

@app.route('/studio-edit')
def editStudio():
    return render_template('studios/edit.html')

# category
@app.route('/categories')
def categories():
    return render_template('/categories/index.html')

@app.route('/category-create')
def createCategories():
    return render_template('/categories/create.html')

@app.route('/category-edit')
def editCategories():
    return render_template('/categories/edit.html')


# anime
@app.route('/animes')
def anime():
    return render_template('/animes/index.html')

@app.route('/anime-create')
def createAnime():
    return render_template('/animes/create.html')

@app.route('/anime-edit')
def editAnime():
    return render_template('/animes/edit.html')