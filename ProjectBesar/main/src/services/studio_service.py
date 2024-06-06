from models import db, Studio

def create_studio(data):
    new_studio = Studio(name=data['name'])
    db.session.add(new_studio)
    db.session.commit()
    return new_studio

def get_all_studios():
    return Studio.query.all()

def get_studio_by_id(studio_id):
    return Studio.query.get_or_404(studio_id)

def update_studio(studio_id, data):
    studio = get_studio_by_id(studio_id)
    studio.name = data.get('name', studio.name)
    db.session.commit()
    return studio

def delete_studio(studio_id):
    studio = get_studio_by_id(studio_id)
    db.session.delete(studio)
    db.session.commit()
    return studio
