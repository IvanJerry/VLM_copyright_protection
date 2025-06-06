from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/chat.html')
def chat():
    return app.send_static_file('chat.html')

@app.route('/model.html')
def model():
    return app.send_static_file('model.html')

@app.route('/watermark.html')
def watermark():
    return app.send_static_file('watermark.html')

@app.route('/settings.html')
def settings():
    return app.send_static_file('settings.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000) 