from flask import Blueprint, render_template

studio_bp = Blueprint('studio', __name__)

@studio_bp.route('/studios')
def studios():
    return render_template('studios/index.html')

@studio_bp.route('/studio-create')
def createStudio():
    return render_template('studios/create.html')

@studio_bp.route('/studio-edit')
def editStudio():
    return render_template('studios/edit.html')
