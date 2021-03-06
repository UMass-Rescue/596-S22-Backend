from datetime import datetime
from fileinput import filename
from re import S
from sqlite3 import Timestamp
from typing import List, Optional, Dict
from xmlrpc.client import DateTime
from app.models import Question
from pydantic import BaseModel
from sqlalchemy import TIMESTAMP, true

# Case Models
class Case(BaseModel):
    id: int
    start_date: datetime
    end_date: Optional[datetime]
    is_active: bool

    class Config:
        orm_mode = True

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

######### Recognized Plates ###############

class RecognizedPlate(BaseModel):
    id: int
    license: str
    time: datetime
    footage_id: int

    class Config:
        orm_mode = True

class CreateRecognizedPlate(BaseModel):
    license: str
    time: datetime

############ License Plate Footage #############

class LicenseFootageBase(BaseModel):
    link: str

class CreateLicenseFootage(LicenseFootageBase):
    pass 

class CreateLicenseFootageObj(BaseModel):
    link: str
    filename: str
    recognized_plates : List[CreateRecognizedPlate]

class LicenseFootage(LicenseFootageBase):
    id: int
    filename: str
    date_uploaded = datetime.now()
    recognized_plates: List[RecognizedPlate] = []

    class Config:
        orm_mode = True

############## Blob Schema ######################

class BlobBase(BaseModel):
    key: str
    file_type: str
    description: str

class CreateBlob(BlobBase):
    pass

class Blob(BaseModel):
    id: int
    key: str
    file_type: str
    description: str
    case_id: int
    date_uploaded = datetime.now()

    class Config:
        orm_mode = True

############## Interview Analyzer Schemas ###############

class CreateQuestion(BaseModel):
    text: str

class Question(BaseModel):
    id: int
    text: str
    case_id: int

    class Config:
        orm_mode = True

class CreateInterviewAnswerNER(BaseModel):
    label: str
    start_index: int
    end_index: int

class InterviewAnswerNER(BaseModel):
    id: int
    label: str
    start_index: int
    end_index: int
    interview_answer_id:  int

    class Config:
        orm_mode = True

class CreateInterviewAnswer(BaseModel):
    question_id: int
    answer: str
    interview_answer_ners: List[CreateInterviewAnswerNER] = []

class InterviewAnswer(BaseModel):
    id: int
    answer: str
    question_id: int
    interview_id: int

    class Config:
        orm_mode = True

class CreateInterviewShell(BaseModel):
    first_name: str
    last_name: str
    address: str
    blob_id: int

class CreateInterview(BaseModel):
    first_name: str
    last_name: str
    address: str
    interview_answers: List[CreateInterviewAnswer] = []

class Interview(BaseModel):
    id: int
    blob_id: int
    is_processed: int
    first_name: str
    last_name: str
    date_uploaded: datetime = datetime.now()
    address: str
    case_id: int

    class Config:
        orm_mode = True

class TranscriberObj(BaseModel):
    blob: Blob
    questions: List[Question]
    interview: Interview

    class Config:
        orm_mode = True
