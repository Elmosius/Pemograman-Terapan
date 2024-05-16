from flask import Flask, jsonify, request, abort
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

app = Flask(__name__)

DATABASE_URL = 'sqlite:///books.db'
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    price = Column(Float, nullable=False)

Base.metadata.create_all(bind=engine)

# nampilin semua
@app.route('/books', methods=['GET'])
def get_books():
    books = session.query(Book).all()
    return jsonify([{"id": book.id, "name": book.name, "price": book.price} for book in books])

# nampilin satu buku
@app.route('/books/<string:name>', methods=['GET'])
def get_book(name):
    book = session.query(Book).filter_by(name=name).first()
    if book is None:
        abort(404, description="Book not found")
    return jsonify({"id": book.id, "name": book.name, "price": book.price})

# buat buku
@app.route('/books', methods=['POST'])
def create_book():
    if not request.json or not 'name' in request.json or not 'price' in request.json:
        abort(400, description="Bad request")
    
    new_book = Book(name=request.json['name'], price=request.json['price'])
    session.add(new_book)
    session.commit()
    return jsonify({"id": new_book.id, "name": new_book.name, "price": new_book.price}), 201


# update buku
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = session.query(Book).filter_by(id=id).first()
    if book is None:
        abort(404, description="Book not found")
    
    if not request.json:
        abort(400, description="Bad request")
    
    book.name = request.json.get('name', book.name)
    book.price = request.json.get('price', book.price)
    
    session.commit()
    return jsonify({"id": book.id, "name": book.name, "price": book.price})


# delete buku
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = session.query(Book).filter_by(id=id).first()
    if book is None:
        abort(404, description="Book not found")
    
    session.delete(book)
    session.commit()
    return jsonify({"result": True})


app.run(debug=True, port=8000)
