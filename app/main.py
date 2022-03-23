from email import message
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route - Root
@app.get("/")
def read_root():
    return {"Rescue" : "Backend"}

# Route - POST - Create User
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email Already Registered")
    return crud.create_user(db=db, user=user)

# Route - GET - Get users
@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# Route - GET - Get user for ID
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Route - POST - Create Item for User ID
@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item, user_id=user_id)

# Route - GET - Get items of all users
@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip, limit=limit)
    return items

# Route - GET - get all messages for all users (test route)
@app.get("/messages/", response_model=List[schemas.Message])
def read_messages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    messages = crud.get_messages(db, skip, limit=limit)
    return messages

# Route - GET - get all messages for specific user
@app.get("/users/{user_id}/messages/", response_model=List[schemas.Message])
def reader_messages_for_user(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    messages = crud.get_messages_for_user(db=db, skip=skip, limit=limit, user_id=user_id)
    return messages

# Route - POST - create new message between user and recipient
@app.post("/messages/", response_model=schemas.Message)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db=db, message=message)

@app.post("/denseCaptionCreate/", response_model=str)
def create_dense_caption(data: schemas.DenseCaptionCreate, db: Session = Depends(get_db)):
    return crud.create_dense_caption(data=data, db=db)

@app.get("/denseCaptionGet/{parent_id}/child", response_model=List[schemas.DenseCaptionChild])
def get_children(parent_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    children = crud.get_children(parent_id=parent_id, db=db, skip=skip, limit=limit)
    return children
    