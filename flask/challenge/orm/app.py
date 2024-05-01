from flask import Flask
from flask_smorest import Api
from db import db
from flask import render_template


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/orm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)



#blueprint setting
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api()

# api.register_blueprint()

@app.route('/manage-board')
def manage_board() :
    return render_template('boards.html')

@app.route('/manage-users')
def manage_users() :
    return render_template('users.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)