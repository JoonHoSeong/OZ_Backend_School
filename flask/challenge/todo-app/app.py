from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from db import db
from flask_migrate import Migrate


app = Flask(__name__)

# 데이터베이스 및 JWT 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' # local db => 파일 형태의 간단한 데이터 베이스
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['API_TITLE'] = 'Todo API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.2'

# db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)
api = Api(app)

# 모델 및 리소스 불러오기 (이후에 정의)
from models import User, Todo
from routes.auth import auth_blp
from routes.todo import todo_blp

# API에 Blueprint 등록
api.register_blueprint(auth_blp)
api.register_blueprint(todo_blp)

@app.route("/")
def index():
    return {"message": "Init Page"}, 200

if __name__ == '__main__':
    app.run(debug=True)