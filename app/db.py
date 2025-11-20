from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# مسیر absolute پوشه پروژه
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))     # hr_api2/app
PROJECT_DIR = os.path.dirname(CURRENT_DIR)                   # hr_api2/

# مسیر فایل .env
ENV_PATH = os.path.join(PROJECT_DIR, ".env")

# چاپ مسیر برای تست (فقط برای دیدن)
print("🔍 Loading .env from:", ENV_PATH)

# لود کردن .env
load_dotenv(ENV_PATH)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(f"❌ .env not loaded! DATABASE_URL is None.\n Tried path: {ENV_PATH}")

# ساخت engine
engine = create_engine(DATABASE_URL, echo=True)

# Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base
Base = declarative_base()

# Dependency برای FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
