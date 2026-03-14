from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# imports for database and models
from app.core.database import SessionLocal
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from app.services.auth_service import hash_password

# Create a router for authentication-related endpoints
router = APIRouter(prefix="/auth", tags=["Auth"])


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Register a new user
@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if the username already exists
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        return {"message": "Username already exists"}
    # Hash the password before storing it
    hashed_password = hash_password(user.password)
    # Create a new user instance
    new_user = User(
        username=user.username,
        password_hash=hashed_password
    )
    # Add the new user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    # Return a success message
    return {"message": "User created successfully"}