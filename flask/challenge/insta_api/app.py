from flask import Flask, request, render_template

app = Flask(__name__)


# 사용자 데이터를 저장하는 리스트
users = [
    {
        "username": "leo",
        "posts": [{"title": "Town House", "likes": 120}]
    },
    {
        "username": "alex",
        "posts": [{"title": "Mountain Climbing", "likes": 350}, {"title": "River Rafting", "likes": 200}]
    },
    {
        "username": "kim",
        "posts": [{"title": "Delicious Ramen", "likes": 230}]
    }
]

@app.get("/")
def index():
    return {"message": "Init Page"}, 200

@app.get("/users")
def get_users():
    # 모든 사용자 정보를 JSON 형태로 반환
    return {"users": users}


@app.post("/users")
def create_user():
    # 클라이언트로부터 받은 JSON 데이터
    request_data = request.get_json()
    # 새 사용자 객체 생성
    new_user = {"username": request_data["username"], "posts": [{"title": "My First Post", "likes": 0}]}
    # 사용자 리스트에 새 사용자 추가
    users.append(new_user)
    # 생성된 사용자 정보와 HTTP 상태코드 201 반환
    return new_user, 201

@app.post("/users/post/<string:username>")
def add_post(username):
    # 클라이언트로부터 받은 JSON 데이터
    request_data = request.get_json()
    # 해당 사용자를 찾아 게시물 추가
    for user in users:
        if user["username"] == username:
            new_post = {"title": request_data["title"], "likes": request_data["likes"]}
            user["posts"].append(new_post)
            return new_post
        
    # 사용자를 찾지 못한 경우 오류 메시지 반환
    return {"message": "User not found"}, 404

@app.get("/users/post/<string:username>")
def get_posts_of_user(username):
    # 특정 사용자의 모든 게시물 반환
    for user in users:
        if user["username"] == username:
            return {"posts": user["posts"]}
    # 사용자를 찾지 못한 경우 오류 메시지 반환
    return {"message": "User not found"}, 404

@app.put("/users/post/like/<string:username>/<string:title>")
def like_post(username, title):
    # 특정 게시물의 좋아요 수 증가
    for user in users:
        if user["username"] == username:
            for post in user["posts"]:
                if post["title"] == title:
                    post["likes"] += 1
                    return post
    # 게시물을 찾지 못한 경우 오류 메시지 반환
    return {"message": "Post not found"}, 404

@app.delete("/users/<string:username>")
def delete_user(username):
    # 전역 users 리스트에서 특정 사용자 삭제
    global users
    users = [user for user in users if user["username"] != username]
    # 삭제 성공 메시지와 HTTP 상태코드 200 반환
    return {"message": "User deleted"}, 200

# 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True)