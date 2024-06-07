from flask import Blueprint, render_template, redirect, url_for, request, flash
import requests

studio_bp = Blueprint('studio', __name__)

@studio_bp.route('/studios')
def studios():
    response = requests.get('http://127.0.0.1:5000/studios')
    studios = response.json()
    return render_template('studios/index.html', studios=studios)

@studio_bp.route('/studios/<int:id>')
def studioById(id):
    response = requests.get(f'http://127.0.0.1:5000/studios/{id}')
    studio = response.json()
    return render_template('studios/index.html', studio=studio)

@studio_bp.route('/studio-create', methods=["GET","POST"])
def createStudio():
    if request.method == 'POST':
        data = request.form.to_dict(flat=False)  
        response = requests.post('http://127.0.0.1:5000/studios', json=data)  
        if response.status_code == 201:
            flash('Studio created successfully!', 'success')
            return redirect(url_for('studio.studios'))
        else:
            flash('Error creating category!', 'danger')
            return redirect(url_for('studio.createCategories'))
    else:
        return render_template('studios/create.html')


@studio_bp.route('/studio-edit/<int:id>',methods=['GET', 'POST'])
def editStudio(id):
    if request.method == 'GET':
        response = requests.get(f'http://127.0.0.1:5000/studios/{id}')
        studio = response.json()

        return render_template('studios/edit.html', studio=studio)
    else:
        data = request.form.to_dict(flat=False)
        response = requests.put(f'http://127.0.0.1:5000/studios/{id}', json=data)
        if response.status_code == 200:
            flash('Studio updated successfully!', 'success')
            return redirect(url_for('studio.studios'))
        else: 
            flash('Error updating studio!', 'danger')
            return redirect(url_for('studio.editStudio', id=id))
        
@studio_bp.route('/studio-delete/<int:id>', methods=['POST'])
def deleteStudio(id):
    response = requests.delete(f'http://127.0.0.1:5000/studios/{id}')
    if response.status_code == 200:
        flash('Studio deleted successfully!', 'success')
    else:
        flash('Error deleting studio!', 'danger')
    return redirect(url_for('studio.studios'))