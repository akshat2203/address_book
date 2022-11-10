from sqlalchemy.orm import Session
from geopy.geocoders import Nominatim
import models
import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_address(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Address).offset(skip).limit(limit).all()


def create_user_address(db: Session, address: schemas.AddressCreate, user_id: int):
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(address.city)
    latitude = 0.00000
    longitude = 0.0000
    if getLoc:
        latitude = getLoc.latitude
        longitude = getLoc.longitude
    db_address = models.Address(city=address.city, latitude=latitude, longitude=longitude, user_id=user_id)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address
