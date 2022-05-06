from email import message
from statistics import mode
from sqlalchemy.orm import Session

from . import models, schemas

# Get User for User ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Get User for Email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Get Users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Create user with username and password
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notReallyHashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get all available items
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

# Create Item with User ID
def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Get all messages for all users
def get_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Message).offset(skip).limit(limit).all()

# Get all messages for specific user
def get_messages_for_user(user_id: int, db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Message).filter(models.Message.sender_id == user_id).offset(skip).limit(limit).all()

# Create Message For Sender (User) and Recipient (User)
def create_message(message: schemas.MessageCreate, db: Session):
    db_message = models.Message(text=message.text, sender_id=message.sender_id, recipient_id=message.recipient_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def create_dense_caption(data: schemas.DenseCaptionCreate, db: Session):
    for entry in data.results:
        db_dense_caption_parent = models.DenseCaptionParent(imageName=entry.img_name)
        db.add(db_dense_caption_parent)
        db.commit()
        db.refresh(db_dense_caption_parent)
        for i in range(len(entry.scores)):
            db_dense_caption_child = models.DenseCaptionChild(score=entry.scores[i], caption=entry.captions[i], bounding_x=entry.boxes[i][0], bounding_y=entry.boxes[i][1], bounding_w=entry.boxes[i][2], bounding_h=entry.boxes[i][3], parent_id=db_dense_caption_parent.id)
            db.add(db_dense_caption_child)
            db.commit()
            db.refresh(db_dense_caption_child)
    return db_dense_caption_parent

def get_children(parent_id: int, db: Session, skip: int = 0, limit: int = 100):
    data = db.query(models.DenseCaptionChild).filter(models.DenseCaptionChild.parent_id==parent_id).offset(skip).limit(limit).all()
    final = {}
    final['children'] = data
    return final

def get_parents(image_name: str, db: Session, skip: int = 0, limit: int = 5):
    data = db.query(models.DenseCaptionParent).filter(models.DenseCaptionParent.imageName==image_name).offset(skip).limit(limit).all()
    final = {}
    final['parents'] = data
    return final

def get_images_keyword(keyword: str, db: Session, skip: int = 0, limit: int = 100):
    data = db.query(models.DenseCaptionChild).filter(models.DenseCaptionChild.caption.contains(keyword)).offset(skip).limit(limit).all()
    final_data = []
    for child in data:
        temp1 = db.query(models.DenseCaptionParent).filter(models.DenseCaptionParent.id==child.parent_id).offset(skip).limit(limit).all()
        final_data.append(temp1[0].imageName)
        #final_data.append(child.parent_id)
    real_final = list(dict.fromkeys(final_data))
    final = {}
    final['temp'] = real_final
    return final