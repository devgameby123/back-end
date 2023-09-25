from fastapi import FastAPI
from domain import UserRepository
from application_service import UserService

app = FastAPI()
user_repository = UserRepository()
user_service = UserService(user_repository)
