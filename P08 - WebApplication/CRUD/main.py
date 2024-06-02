from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data disimpan di memory menggunakan list
data = []

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        data.append({'id': len(data) + 1, 'name': name})
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    item = next((item for item in data if item['id'] == id), None)
    if request.method == 'POST':
        if item:
            item['name'] = request.form['name']
            return redirect(url_for('index'))
    return render_template('update.html', item=item)

@app.route('/delete/<int:id>')
def delete(id):
    global data
    data = [item for item in data if item['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
