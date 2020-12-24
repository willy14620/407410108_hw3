from flask import Flask, render_template
import json
from flask.globals import request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/store_data', methods=['GET', 'POST'])
def store_data():
    if request.method == 'POST':
        print(request.form)
        with open('./data/user_pwd.json', 'a', encoding='utf-8', newline='') as file:
            data = {'username': request.form['username'],
                    'password': request.form['password']}
            file.write(json.dumps(data, indent=4))
        return render_template('index.html')
    else:
        return render_template('form.html')


app.run()
