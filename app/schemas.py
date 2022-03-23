from datetime import datetime
from typing import List, Optional, Dict, Union
from pydantic import BaseModel
from sqlalchemy import TIMESTAMP, true

# Item Models
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

# User Models
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True

# Message Models
class MessageCreate(BaseModel):
    text: str
    sender_id: int
    recipient_id: int

class Message(BaseModel):
    id: int
    text: str
    time: datetime = datetime.now()
    sender_id: int
    recipient_id: int

    class Config:
        orm_mode = True

class DenseCaptionCreate(BaseModel):
    opt: Dict[str, Union[str, int]]
    results: List[Dict[str, Union[str, List[float], List[str], List[List[float]]]]]

class DenseCaptionChild(BaseModel):
    id: int
    caption: str
    score: float
    bounding_x: float
    bounding_y: float
    bounding_w: float
    bounding_h: float
    parent_id: int

    class Config:
        orm_mode = True