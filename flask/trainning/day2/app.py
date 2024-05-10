from flask import Flask, request

app = Flask(__name__)

datas = [{"name": "item1", "price": 10}]

@app.route('/datas', methods=['GET'])
def get_datas():
    return {'datas':datas}

@app.route('/datas', methods=['POST'])
def create_data():
    request_data = request.get_json()
    datas.append(request_data)
    return request_data, 201