import uuid
from app.schemas.user import UserResponse
from app.core.logger import setup_logger

logger = setup_logger(__name__)

class MockUser:
    def __init__(self):
        self.id = uuid.uuid4()
        self.username = "test"
        self.email = "test@gmail.com"

try:
    resp = UserResponse.model_validate(MockUser())
    logger.info(f"Success: {resp}")
except Exception as e:
    logger.error(f"Error: {e}")
