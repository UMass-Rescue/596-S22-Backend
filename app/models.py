from datetime import datetime
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base

class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    end_date = Column(TIMESTAMP(timezone=False))
    is_active = Column(Boolean, default=True)

    blobs = relationship("Blob", back_populates="case")
    questions = relationship("Question", back_populates="case")
    interviews = relationship("Interview", back_populates="case")

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

class Blob(Base):
    __tablename__ = "blobs"

    id = Column(Integer, primary_key=True, index=True)
    date_uploaded = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    description = Column(String)
    key = Column(String, index=True)
    file_type = Column(String, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"))

    case = relationship("Case", back_populates="blobs")

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    case_id = Column(Integer, ForeignKey("cases.id"))

    case = relationship("Case", back_populates="questions")

class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    date_uploaded = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    address = Column(String)
    case_id = Column(Integer, ForeignKey("cases.id"))

    case = relationship("Case", back_populates="interviews")
    interview_answers = relationship("InterviewAnswers", back_populates="interviews")

class InterviewAnswer(Base):
    __tablename__ = "interview_answers"

    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String)
    question_id = Column(Integer, ForeignKey("questions.id"))
    interview_id = Column(Integer, ForeignKey("interviews.id"))

    question = relationship("Question", back_populates="interview_answers")
    interview = relationship("Interview", back_populates="interview_answers")

    interview_answer_ners = relationship("InterviewAnswerNER", back_populates="interview_answers")

class InterviewAnswerNER(Base):
    __tablename__ = "interview_answer_ners"

    id = Column(Integer, primary_key=True, index=True)
    ner_label = Column(String)
    start_index = Column(Integer)
    end_index = Column(Integer)
    interview_answer_id = Column(Integer, ForeignKey("interview_answers.id"))

    interview_answer = relationship("InterviewAnswers", back_populates="interview_answer_ners")

