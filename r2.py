from fastapi import HTTPException
from app.utils.auth import fake_users_db

@router.post("/register/")
async def register_user(username: str, password: str):
        # Check if the username already exists
        if username in fake_users_db:
            raise HTTPException(status_code=400, detail="Username already exists")

        # Create a new user entry in the database
        fake_users_db[username] = {"username": username, "password": password}

        return {"message": "User registered successfully"}



@router.get("/user/{username}/")
async def get_user_details(username: str):
    # Check if the user exists in the database
    user = fake_users_db.get(username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Return user details
    return {"username": user["username"]}