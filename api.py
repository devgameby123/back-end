from fastapi import HTTPException
from adapters import app, user_service


@app.post("/users/")
async def create_user(username: str, email: str):
    user_id = 1  # Generate or fetch a user ID
    user_service.create_user(user_id, username, email)
    return {"message": "User created successfully"}


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/")
def root():
    return {"message": "Hello sir"}
