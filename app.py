import os.path
from flask import Flask, render_template

app = Flask(__name__, template_folder='static/templates/')

service = os.environ.get('K_SERVICE', 'Unknown service')
revision = os.environ.get('K_REVISION', 'Unknown revision')

@app.route('/', methods=['GET'])
def root():
    return render_template('index.html',
    Service=service,
    Revision=revision)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')