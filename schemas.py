from typing import List, Union

from pydantic import BaseModel


class AddressBase(BaseModel):
    city: str


class AddressCreate(AddressBase):
    pass


class Address(AddressBase):
    id: int
    user_id: int
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    address: List[Address] = []

    class Config:
        orm_mode = True
