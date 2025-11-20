from datetime import date, datetime
from typing import Optional, List
from pydantic import BaseModel


# ------- USER --------

class UserBase(BaseModel):
    name: str
    family_name: str
    birthdate: Optional[date] = None
    gender: Optional[str] = None
    entry_date: Optional[date] = None
    exit_date: Optional[date] = None
    status: Optional[str] = None
    authent_user_uuid: Optional[str] = None


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: Optional[str] = None
    family_name: Optional[str] = None
    birthdate: Optional[date] = None
    gender: Optional[str] = None
    entry_date: Optional[date] = None
    exit_date: Optional[date] = None
    status: Optional[str] = None
    authent_user_uuid: Optional[str] = None


class UserRead(UserBase):
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# ------- RESERVATION --------

class ReservationBase(BaseModel):
    user_id: int
    resource_id: int
    start_at: datetime
    end_at: datetime
    status: Optional[str] = None
    purpose: Optional[str] = None


class ReservationCreate(ReservationBase):
    pass


class ReservationUpdate(BaseModel):
    resource_id: Optional[int] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    status: Optional[str] = None
    purpose: Optional[str] = None
    cancelled_at: Optional[datetime] = None


class ReservationRead(ReservationBase):
    reservation_id: int
    created_by: Optional[int] = None
    cancelled_at: Optional[datetime] = None

    class Config:
        orm_mode = True
