from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_TYPE = "mysql+pymysql"
DB_USER = "root"
DB_PASS = "Admin%40123"
DB_HOST_PORT = "localhost:3306"
DB_NAME = "bloghub_db"

DATABASE_URL = f"{DB_TYPE}://{DB_USER}:{DB_PASS}@{DB_HOST_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()