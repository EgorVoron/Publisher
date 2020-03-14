from flask import Flask, send_from_directory
import logging
from flask_cors import CORS

app = Flask(__name__)

logging.getLogger('flask_cors').level = logging.DEBUG
CORS(app, supports_credentials=True, origin='http://localhost:8080')


@app.route('/', methods=['GET'])
def main():
    return send_from_directory(filename='templates/main.html', directory='')


@app.route('/taylor', methods=['GET'])
def taylor():
    return send_from_directory(filename='templates/taylor.html', directory='')


@app.route('/virus', methods=['GET'])
def virus():
    return send_from_directory(filename='templates/virus.html', directory='')


@app.route('/fun_dist', methods=['GET'])
def fun_dist():
    return send_from_directory(filename='templates/fun_dist.html', directory='')


@app.route('/attractor', methods=['GET'])
def attractor():
    return send_from_directory(filename='templates/attractor.html', directory='')


@app.route('/waves', methods=['GET'])
def waves():
    return send_from_directory(filename='templates/waves.html', directory='')

print('http://localhost:8010/')
app.run(port=8010, host='0.0.0.0', debug=True)
