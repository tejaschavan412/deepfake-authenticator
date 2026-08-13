from app.db.database import engine
from sqlalchemy import text
from app.core.logger import setup_logger

logger = setup_logger(__name__)
def fix_alembic():
    with engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS alembic_version;"))
        conn.commit()
        logger.info("Dropped alembic_version table successfully!")

if __name__ == "__main__":
    fix_alembic()
