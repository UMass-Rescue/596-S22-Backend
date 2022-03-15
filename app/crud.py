from email import message
from statistics import mode
from sqlalchemy.orm import Session
import os

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

# Create License Footage using specified Link
def create_license_footage_with_link(license_footage: schemas.CreateLicenseFootage, db: Session):

    # Add License Footage Object
    db_message = models.LicenseFootage(filename=filename, link=license_footage.link)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    
    # Insert code to get identify all license plates and their attachment.

    ####################
    ## YOUR CODE HERE ##
    ####################

    # return type - Array of License plates and their occurance - [RecognizedPlate]
    # Instantiate footage_id - using db_message.id

    recognized_plates = []
    filename = os.path.basename(license_footage.link)

    # Add Plates individually
    for plate in recognized_plates:
        db.add(plate)
        db.commit()
        db.refresh(plate)

    return license_footage

# Create License Footage with Specified Object
def create_license_footage_with_obj(license_footage: schemas.LicenseFootage, db: Session):

    # Add the parent information
    db_parent_message = models.LicenseFootage(filename=license_footage.filename, link=license_footage.link)
    db.add(db_parent_message)
    db.commit()
    db.refresh(db_parent_message)

    parent_id = db_parent_message.id

    # Add the child information
    for plate in license_footage.recognized_plates:
        db_child_message = models.RecognizedPlate(license=plate.license, time=plate.time, footage_id=parent_id)
        db.add(db_child_message)
        db.commit()
        db.refresh(db_child_message)

    return db_parent_message

# Get all license plates for that license_footage id
def get_license_plates_for_filename(footage_id: int, db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RecognizedPlate).filter(models.RecognizedPlate.footage_id == footage_id).offset(skip).limit(limit).all()

# Create Interview object with audio file name
##THIS IS ASSUMING AUDIO FILES HAS ALREADY BEEN SAVED TO DATABASE
def create_interview(audio_filename: str, db: Session):

    # Insert code to retrieve audio file from db

    ####################
    ## YOUR CODE HERE ##
    ####################

    # return type - audio file of interview
    # NEED TO FIGURE OUT IF AUDIO FILE OR PATH OF FILE SHOULD BE RETURNED

    #following this post: https://stackoverflow.com/questions/64558200/python-requests-in-docker-compose-containers
    path = "the path to the server" + "/sendTranscription"
    response = session.post(path, json={"audio_filename": audio_filename})

    #get the full text transcription from the response
    reponse_json = json.loads(response.text)
    full_text = reponse_json['transcription']

    # Add Interview object
    db_message = models.Interview(filename=filename, full_name = interview.full_name,
                                  created_at = interview.created_at,
                                  address = interview.address,
                                  case = interview.case, full_text = full_text)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)

    return db_message

# Create Interview object with audio file name
##THIS IS ASSUMING AUDIO FILES HAS ALREADY BEEN SAVED TO DATABASE
def analyze_interview(case: int, audio_filename: str, db: Session):

    #get full text for this interview
    full_text = db.query(models.Interview).filter(models.Interview.filename == audio_filename).offset(skip).limit(limit).all()

    #get list of questions for this interview
    questions = db.query(models.Question).filter(models.Question.case == case).offset(skip).limit(limit).all()
    add_questions = db.query(models.Additional_Question).filter(models.Additional_Question.interview_id == question_answer_pair.interview_id).offset(skip).limit(limit).all()
    questions = questions + add_questions

    #following this post: https://stackoverflow.com/questions/64558200/python-requests-in-docker-compose-containers
    path = "the path to the server" + "/analyzeText"
    response = session.post(path, json={"full_text": full_text, "questions": questions})

    #get the json from the response
    reponse_json = json.loads(response.text)
    all_pairs = reponse_json['transcription']

    # Add each pair and NER
    # CAN I ADD MULTIPLE OBJECTS TO THE DB IN ONE COMMIT?
    for pair in all_pairs:
        db_pair_message = models.Question_Answer_Pair(interview_id=interview.id, question=pair['question'], answer=pair['answer'])
        db.add(db_pair_message)
        db.flush()  #allows for the primary key of the pair to be generated
        for ner in pair['ner']:
            db_ner_message = models.Answer_NER(question_answer_pair_id=db_pair_message.id, label=ner['label'], answer=pair['answer'])
            db.add(db_ner_message)
        db.commit()
        db.refresh(db_pair_message)

    return all_pairs

# Get all question and answer pairs for an interview
def get_question_answer_pairs(interview_id: int, db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Question_Answer_Pair).filter(models.Question_Answer_Pair.interview_id == interview_id).offset(skip).limit(limit).all()

# Get all ner objects for an answer
def get_ners_for_answer(question_answer_pair_id: int, db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Answer_NER).filter(models.Answer_NER.question_answer_pair_id == question_answer_pair_id).offset(skip).limit(limit).all()
