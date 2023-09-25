class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email


class UserRepository:
    def get_user_by_id(self, user_id):
        pass

    def create_user(self, user):
        pass
