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

#---------------------------------------------------------

 
class CreateOpt(BaseModel):
    output_dir: str
    num_to_draw: int
    final_nms_thresh: float
    use_cudnn: int
    text_size: int
    max_images: int
    gpu: int
    splits_json: str
    vg_img_root_dir: str
    checkpoint: str
    num_proposals: int
    rpn_nms_thresh: float
    image_size: int
    input_image: str
    input_split: str
    box_width: int
    input_dir: str
    output_vis_dir: str
    output_vis: int


class CreateResult(BaseModel):
    img_name: str
    scores: List[float]
    captions: List[str]
    boxes: List[List[float]]


class DenseCaptionCreate(BaseModel):
    opt: CreateOpt
    results: List[CreateResult]


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


class DenseCaptionParent(BaseModel):
    id: int
    imageName: str

    class Config:
        orm_mode = True
