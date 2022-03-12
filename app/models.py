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