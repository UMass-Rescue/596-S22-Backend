from datetime import datetime
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    messages = relationship("Message", back_populates="sender")
    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    time = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    sender_id = Column(Integer, ForeignKey("users.id"))
    recipient_id = Column(Integer, index=True)

    sender = relationship("User", back_populates="messages")

class LicenseFootage(Base):
    __tablename__ = "license_footage"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    date_uploaded = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    link = Column(String)

    recognized_plates = relationship("RecognizedPlate", back_populates="footage")

class RecognizedPlate(Base):
    __tablename__ = "recognized_plates"

    id = Column(Integer, primary_key=True, index=True)
    license = Column(String, index=True)
    time = Column(TIMESTAMP(timezone=False))
    footage_id = Column(Integer, ForeignKey("license_footage.id"))

    footage = relationship("LicenseFootage", back_populates="recognized_plates")

class Interview(Base):
    __tablename__ = "interview"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    created_at = Column(TIMESTAMP(timezone=False))
    address = Column(String, index=True)
    case = Column(Integer, ForeignKey("license_footage.id"))
    full_text = Column(String, index=True)

    interview = relationship("Interview", back_populates="interview")

class Question_Answer_Pair(Base):
    __tablename__ = "question_answer_pair"

    id = Column(Integer, primary_key=True, index=True)
    interview_id = Column(Integer, ForeignKey("interview.id")) ##Please check if this is correct
    question = Column(String, index=True)
    answer = Column(String, index=True)

    question_answer_pair = relationship("Question_Answer_Pair", back_populates="question_answer_pair")

class Question(Base):
    __tablename__ = "question"

    case = Column(Integer, index=True)
    question = Column(String, index=True)

question = relationship("Question", back_populates="question")

class Additional_Question(Base):
    __tablename__ = "additional_question"

    interview_id = Column(Integer, ForeignKey("interview.id")) ##Please check if this is correct
    question = Column(String, index=True)

    additional_question = relationship("Additional_Question", back_populates="additional_question")

class Answer_NER(Base):
    __tablename__ = "answer_ner"

    question_answer_pair_id = Column(Integer, ForeignKey("question_answer_pair.id")) ##Please check if this is correct
    ner_label = Column(String, index=True)
    start_index = Column(Integer, index=True)
    end_index = Column(Integer, index=True)

    answer_ner = relationship("Answer_NER", back_populates="answer_ner")