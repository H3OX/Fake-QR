import os.path
from flask import Flask, render_template

app = Flask(__name__, template_folder='static/templates/')


@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
