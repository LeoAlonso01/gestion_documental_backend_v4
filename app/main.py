from fastapi import FastAPI
from app.core.database import engine, Base
import app.models  # Importar modelos para que se registren con SQLAlchemy

# import routers
from app.api.routes import auth_routes

# from app.api.routes import user_routes
app = FastAPI()

# create database tables if they don't exist
Base.metadata.create_all(bind=engine)

# include routers
app.include_router(auth_routes.router)

# Define a simple root endpoint to verify that the backend is running
@app.get("/")
def read_root():
    return {"message": "Backend is running for the first time!"}