from flask import Flask, jsonify, render_template
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# 사용자 정보
users = {
    "admin": "secret",
    "guest": "guest"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

@app.route('/protected')
@auth.login_required
def protected():
    return render_template('secret.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)