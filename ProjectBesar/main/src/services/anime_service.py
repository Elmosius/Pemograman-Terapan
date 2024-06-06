from models import db, Anime, Genre

def create_anime(data):
    new_anime = Anime(
        title=data['title'],
        author=data['author'],
        image=data['image'],
        episodes=data['episodes'],
        synopsis=data['synopsis'],
        season=data['season'],
        status=data['status'],
        rating=data['rating'],
        studio_id=data['studio_id']
    )
    if 'genres' in data:
        for genre_name in data['genres']:
            genre = Genre.query.filter_by(name=genre_name).first()
            if genre:
                new_anime.genres.append(genre)
    db.session.add(new_anime)
    db.session.commit()
    return new_anime

def get_all_animes():
    return Anime.query.all()

def get_anime_by_id(anime_id):
    return Anime.query.get_or_404(anime_id)

def update_anime(anime_id, data):
    anime = get_anime_by_id(anime_id)
    anime.title = data.get('title', anime.title)
    anime.author = data.get('author', anime.author)
    anime.image = data.get('image', anime.image)
    anime.episodes = data.get('episodes', anime.episodes)
    anime.synopsis = data.get('synopsis', anime.synopsis)
    anime.season = data.get('season', anime.season)
    anime.status = data.get('status', anime.status)
    anime.rating = data.get('rating', anime.rating)
    anime.studio_id = data.get('studio_id', anime.studio_id)
    if 'genres' in data:
        anime.genres.clear()
        for genre_name in data['genres']:
            genre = Genre.query.filter_by(name=genre_name).first()
            if genre:
                anime.genres.append(genre)
    db.session.commit()
    return anime

def delete_anime(anime_id):
    anime = get_anime_by_id(anime_id)
    db.session.delete(anime)
    db.session.commit()
    return anime
