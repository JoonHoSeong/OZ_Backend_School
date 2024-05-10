from flask import Flask
from flask_login import LoginManager
from models import User
from routes import configure_routes

# 'routes' 모듈을 임포트하기 전에 'app'과 'login_manager' 객체를 생성해야 함
app = Flask(__name__)
app.secret_key = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# 이제 'routes' 모듈을 임포트
configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)