from flask import Flask, jsonify, request


app = Flask(__name__)
class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def json(self):
        return {'name': self.name, 'price': 
        self.price}
books = {}

@app.route('/books', methods=['GET'])
def get_books():
    if len(books) > 0:
        return jsonify({'books': books}), 200
 
    return jsonify({'message': 'No books found'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(data['name'], data['price'])
    books[new_book.name] = new_book.price
    return jsonify(new_book.json()), 201


@app.route('/books/<string:name>', 
methods=['GET'])
def get_book(name):
    if name in books:
        return jsonify({name: books[name]}), 200
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books/<string:name>', 
methods=['PUT'])
def update_book(name):
    data = request.get_json()
    if name in books:
        books[name] = data['price']
        return jsonify({name: books[name]}), 200
    return jsonify({'message': 'Book not found'}), 404


@app.route('/books/<string:name>', 
methods=['DELETE'])
def delete_book(name):
    if name in books:
        del books[name]
        return jsonify({'message': 'Book deleted'}), 200
    return jsonify({'message': 'Book not found'}), 404

app.run(debug=True, port=8090)