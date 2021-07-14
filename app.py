import os.path
from flask import Flask, render_template

app = Flask(__name__, template_folder='static/templates/')


@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')
    