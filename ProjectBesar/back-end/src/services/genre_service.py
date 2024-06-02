from models import db, Genre

def create_genre(data):
    new_genre = Genre(name=data['name'])
    db.session.add(new_genre)
    db.session.commit()
    return new_genre

def get_all_genres():
    return Genre.query.all()

def get_genre_by_id(genre_id):
    return Genre.query.get_or_404(genre_id)

def update_genre(genre_id, data):
    genre = get_genre_by_id(genre_id)
    genre.name = data.get('name', genre.name)
    db.session.commit()
    return genre

def delete_genre(genre_id):
    genre = get_genre_by_id(genre_id)
    db.session.delete(genre)
    db.session.commit()
    return genre
