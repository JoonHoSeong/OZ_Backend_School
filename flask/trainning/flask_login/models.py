from flask_login import UserMixin

users = {'admin': {'password': 'secret'}}

class User(UserMixin):
    def __init__(self, username):
        self.id = username

    @staticmethod
    def get(user_id):
        if user_id in users:
            return User(user_id)
        return None