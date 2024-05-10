from flask import Blueprint, jsonify, request, render_template
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from models.user import User

user_bp = Blueprint('user', __name__)

# 임시 사용자 데이터
users = {
    'user1': User('1', 'user1', 'pw123'),
    'user2': User('2', 'user2', 'pw123')
}

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        user = users.get(username)
        if user and user.password == password:
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)
            return jsonify(access_token=access_token, refresh_token=refresh_token)
        else:
            return jsonify({"msg": "Bad username or password"}), 401
    else:
        return render_template('login.html')


@user_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@user_bp.route('/protected_page')
def protected_page():
    return render_template('protected.html')

from flask_jwt_extended import get_jwt
from blocklist import add_to_blocklist  # 블랙리스트 관리 모듈 임포트
@user_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    add_to_blocklist(jti)  # jti를 블랙리스트에 추가
    return jsonify({"msg": "Successfully logged out"}), 200