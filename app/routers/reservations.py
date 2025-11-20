from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..db import get_db
from .. import models, schemas

router = APIRouter(
    prefix="/reservations",
    tags=["reservations"],
)


@router.get("/", response_model=List[schemas.ReservationRead])
def list_reservations(db: Session = Depends(get_db)):
    reservations = db.query(models.Reservation).all()
    return reservations


@router.get("/{reservation_id}", response_model=schemas.ReservationRead)
def get_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = (
        db.query(models.Reservation)
        .filter(models.Reservation.reservation_id == reservation_id)
        .first()
    )
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation


@router.post("/", response_model=schemas.ReservationRead, status_code=status.HTTP_201_CREATED)
def create_reservation(res_in: schemas.ReservationCreate, db: Session = Depends(get_db)):
    # Check if User exists
    user = db.query(models.User).filter(models.User.user_id == res_in.user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="User does not exist")

    # Check if Resource exists
    resource = (
        db.query(models.Resource)
        .filter(models.Resource.resource_id == res_in.resource_id)
        .first()
    )
    if not resource:
        raise HTTPException(status_code=400, detail="Resource does not exist")

    reservation = models.Reservation(**res_in.dict())
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation


@router.put("/{reservation_id}", response_model=schemas.ReservationRead)
def update_reservation(
    reservation_id: int,
    res_in: schemas.ReservationUpdate,
    db: Session = Depends(get_db),
):
    reservation = (
        db.query(models.Reservation)
        .filter(models.Reservation.reservation_id == reservation_id)
        .first()
    )
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")

    for field, value in res_in.dict(exclude_unset=True).items():
        setattr(reservation, field, value)

    db.commit()
    db.refresh(reservation)
    return reservation


@router.delete("/{reservation_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = (
        db.query(models.Reservation)
        .filter(models.Reservation.reservation_id == reservation_id)
        .first()
    )
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")

    db.delete(reservation)
    db.commit()
    return
