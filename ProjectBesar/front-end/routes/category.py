from flask import Blueprint, render_template

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories')
def categories():
    return render_template('categories/index.html')

@category_bp.route('/category-create')
def createCategories():
    return render_template('categories/create.html')

@category_bp.route('/category-edit')
def editCategories():
    return render_template('categories/edit.html')
