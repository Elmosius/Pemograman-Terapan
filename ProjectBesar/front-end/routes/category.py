from flask import Blueprint, render_template, redirect, url_for, request, flash
import requests

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories')
def categories():
    response = requests.get('http://127.0.0.1:5000/genres')
    genres = response.json()
    return render_template('categories/index.html', genres=genres)

@category_bp.route('/categories/<int:id>')
def categoryById(id):
    response = requests.get(f'http://127.0.0.1:5000/genres/{id}')
    genres = response.json()
    return render_template('categories/index.html', genres=genres)

@category_bp.route('/category-create',methods=['GET', 'POST'])
def createCategory():
    if request.method == 'POST':
        data = request.form.to_dict(flat=False)  
        response = requests.post('http://127.0.0.1:5000/genres', json=data)  
        if response.status_code == 201:
            flash('Category created successfully!', 'success')
            return redirect(url_for('category.categories'))
        else:
            flash('Error creating category!', 'danger')
            return redirect(url_for('category.createCategories'))
    else:
        return render_template('categories/create.html')

@category_bp.route('/category-edit/<int:id>',methods=['GET', 'POST'])
def editCategory(id):
    if request.method == 'GET':
        genres_response = requests.get(f'http://127.0.0.1:5000/genres/{id}')
        genre = genres_response.json()

        return render_template('categories/edit.html', genre=genre)
    else:
        data = request.form.to_dict(flat=False)
        response = requests.put(f'http://127.0.0.1:5000/genres/{id}', json=data)
        if response.status_code == 200:
            flash('Category updated successfully!', 'success')
            return redirect(url_for('category.categories'))
        else:
            flash('Error updating category!', 'danger')
            return redirect(url_for('category.editCategories', id=id))

@category_bp.route('/category-delete/<int:id>', methods=['POST'])
def deleteCategory(id):
    response = requests.delete(f'http://127.0.0.1:5000/genres/{id}')
    if response.status_code == 200:
        flash('Genre deleted successfully!', 'success')
    else:
        flash('Error deleting genre!', 'danger')
    return redirect(url_for('category.categories'))
