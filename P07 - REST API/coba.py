from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/', methods=['GET'])

def hello():
    return jsonify({'message': 'Hello World!'})

app.run(debug=True, port=8090)