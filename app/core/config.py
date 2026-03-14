import os

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "./uploads")
    MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "openai")

config = Config()