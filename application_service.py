from domain import User, UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_id, username, email):
        user = User(user_id, username, email)
        self.user_repository.create_user(user)

    def get_user(self, user_id):
        return self.user_repository.get_user_by_id(user_id)
