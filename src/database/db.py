from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL for connecting to the PostgreSQL database using psycopg2 driver.
# "postgresql+psycopg2://<username>:<password>@<host>:<port>/<database_name>"
SQLALCHEMY_DATABASE_URL = (
    "postgresql+psycopg2://postgres:aN9e94poEi@"
    "localhost:5432/rest_app"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Dependency function for FastAPI to generate database sessions.
    This function creates a new session using SessionLocal, yields it for use,
    and ensures that the session is closed after the request finishes.
    """
    db = SessionLocal()
    try:
        yield db  # Provide the session to the endpoint.
    finally:
        db.close()  # Ensure the session is closed after use.
