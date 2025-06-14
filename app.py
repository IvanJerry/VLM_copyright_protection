from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)
app.secret_key = os.urandom(24)  # 用于session加密

# 模拟用户数据库
USERS = {
    'admin': {'password': 'admin123', 'type': 'admin'},
    'user': {'password': 'user123', 'type': 'user'}
}

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return app.send_static_file('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return app.send_static_file('login.html')
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    login_type = data.get('type')

    if username in USERS and USERS[username]['password'] == password and USERS[username]['type'] == login_type:
        session['username'] = username
        session['type'] = login_type
        return jsonify({'success': True})
    return jsonify({'success': False, 'message': '用户名或密码错误'})

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/chat.html')
def chat():
    if 'username' not in session:
        return redirect(url_for('login'))
    return app.send_static_file('chat.html')

@app.route('/model.html')
def model():
    if 'username' not in session:
        return redirect(url_for('login'))
    return app.send_static_file('model.html')

@app.route('/watermark.html')
def watermark():
    if 'username' not in session:
        return redirect(url_for('login'))
    return app.send_static_file('watermark.html')

@app.route('/settings.html')
def settings():
    if 'username' not in session:
        return redirect(url_for('login'))
    return app.send_static_file('settings.html')

@app.route('/admin.html')
def admin():
    if 'username' not in session or session.get('type') != 'admin':
        return redirect(url_for('login'))
    return app.send_static_file('admin.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    