from config import db

anime_genre = db.Table('anime_genre',
    db.Column('anime_id', db.Integer, db.ForeignKey('anime.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key=True)
)

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Genre {self.name}>'

class Studio(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<Studio {self.name}>'

class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    episodes = db.Column(db.Integer, nullable=False)
    synopsis = db.Column(db.Text, nullable=True)
    season = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(10), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genres = db.relationship('Genre', secondary=anime_genre, backref=db.backref('animes', lazy=True))
    studio_id = db.Column(db.Integer, db.ForeignKey('studio.id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    studio = db.relationship('Studio', backref=db.backref('animes', lazy=True))

    def __repr__(self):
        return f'<Anime {self.title}>'
