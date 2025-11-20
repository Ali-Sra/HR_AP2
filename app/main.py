from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db import engine
from . import models
from .routers import users, reservations

# --- ایجاد جداول در دیتابیس ---
models.Base.metadata.create_all(bind=engine)

# --- ایجاد اپ ---
app = FastAPI(
    title="HR & Reservation Backend",
    version="1.0.0"
)

# --- فعال کردن CORS برای Angular ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200",
        "*"   # اگر خواستی محدودش می‌کنی
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- روت اصلی ---
@app.get("/")
def root():
    return {"message": "HR System Backend Running 🚀"}


# --- ثبت Routerها ---
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(reservations.router, prefix="/reservations", tags=["Reservations"])
