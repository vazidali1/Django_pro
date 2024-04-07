from fastapi import APIRouter, HTTPException

router = APIRouter()

# Dummy database to store user details
db = {}

@router.post("/register/")
async def register_user(user_data: dict):
    """
    Register a new user.
    """
    # Assuming user_data contains necessary user details such as username, email, password, etc.
    username = user_data.get("username")
    if username in db:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # Store user data in database
    db[username] = user_data
    return {"message": "User registered successfully"}

@router.get("/user/{username}/")
async def get_user_details(username: str):
    """
    Get details of a specific user.
    """
    if username not in db:
        raise HTTPException(status_code=404, detail="User not found")
    
    return db[username]
