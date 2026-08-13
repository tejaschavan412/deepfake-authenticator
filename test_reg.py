import asyncio
from app.db.database import SessionLocal
from app.schemas.user import UserRegister
from app.services.auth_service import AuthService
from app.core.security import hash_password
from app.core.logger import setup_logger

logger = setup_logger(__name__)

db = SessionLocal()
user = UserRegister(username="testuser2", email="test2@gmail.com", password="pass4132")
try:
    AuthService.register_user(db, user)
    logger.info("Success")
except Exception as e:
    logger.error(f"Error: {type(e)} {e}")
