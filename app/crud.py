from datetime import datetime
from email import message
from statistics import mode
from sqlalchemy.orm import Session
from fastapi import  HTTPException
import os
import request

from . import models, schemas

# Create Case
def create_case(db: Session):
    db_case = models.Case(start_date=datetime.now())
    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    print(db_case.end_date)
    return db_case

# Get all cases available
def get_all_cases(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Case).offset(skip).limit(limit).all()

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

# Get all footage for a plate_id
def get_footage_for_plate_id(license_plate_number: str, db: Session, skip: int = 0, limit: int = 0):
    data = {}

    # Get all the plates
    plates = db.query(models.RecognizedPlate).filter(models.RecognizedPlate.license == license_plate_number).offset(skip).limit(limit).all()

    # for all discovered plates, add unique footage to dictionary
    for plate in plates:
        if plate.footage_id not in data:
            data[plate.footage_id] = db.query(models.LicenseFootage).filter(models.LicenseFootage.id == plate.footage_id).offset(skip).limit(limit).all()[0]

    return list(data.values())

################## BLOB CRUDS #########################

# Get all blobs with case id
def get_all_blobs_for_case(case: int, db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.Blob).filter(models.Blob.case_id == case).offset(skip).limit(limit).all()

# Create blob object and upload to database
def create_blob_with(case: int, blob: schemas.CreateBlob, db: Session):
    db_blob = models.Blob(key=blob.key, file_type=blob.file_type, description=blob.description, case_id=case)
    db.add(db_blob)
    db.commit()
    db.refresh(db_blob)
    return db_blob

############ INTERVIEW QUESTION CRUDS ###################

def create_question_with(case: int, question: schemas.CreateQuestion, db: Session):
    db_question = models.Question(case_id=case, text=question.text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def get_questions_for(case: int, db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.Question).filter(models.Question.case_id == case).offset(skip).limit(limit).all()

def create_interview_shell_for(case: int, db: Session, interviewShell: schemas.CreateInterviewShell):
    # Create interview
    db_interview = models.Interview(blob_id=interviewShell.blob_id, first_name=interviewShell.first_name, last_name=interviewShell.last_name, address=interviewShell.address, case_id=case)
    db.add(db_interview)
    db.commit()
    db.refresh(db_interview)

    # Create Model to send to Transcriber
    blob = db.query(models.Blob).filter(models.Blob.id == interviewShell.blob_id).first()
    questions = db.query(models.Question).all()

    transcriber_obj = schemas.TranscriberObj(blob=blob, questions=questions, interview=db_interview)

    # Send Transcriber obj to service
    result = request.post("www.localhost:8000/sendTranscription/", data=transcriber_obj)

    if result.status_code > 400:
        raise HTTPException(status_code=404, detail="Unable to send to transcriber")
    
    return db_interview

def patch_interview_shell_for(case: int, db: Session, interview: schemas.Interview):
    pass

def create_interview_with(case: int, db: Session, interview: schemas.CreateInterview):
    # Create Interview
    db_interview = models.Interview(first_name=interview.first_name, last_name=interview.last_name, address=interview.address, case_id=case)
    db.add(db_interview)
    db.commit()
    db.refresh(db_interview)

    # Create Interview Answer Objects
    for interviewAnswer in interview.interview_answers:
        db_interview_answer = models.InterviewAnswer(answer=interviewAnswer.answer, question_id=interviewAnswer.question_id, interview_id=db_interview.id)
        db.add(db_interview_answer)
        db.commit()
        db.refresh(db_interview_answer)

        # Create Interview Answer NER Objects
        for interviewAnswerNER in interviewAnswer.interview_answer_ners:
            db_interview_answer_ner = models.InterviewAnswerNER(label=interviewAnswerNER.label, start_index=interviewAnswerNER.start_index, end_index=interviewAnswerNER.end_index, interview_answer_id=db_interview_answer.id)
            db.add(db_interview_answer_ner)
            db.commit()
            db.refresh(db_interview_answer_ner)

    return db_interview

def get_interview_for(case: int, db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.Interview).filter(models.Interview.case_id == case).offset(skip).limit(limit).all()

def get_interview_answers_for(interview_id: int, db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.InterviewAnswer).filter(models.InterviewAnswer.interview_id == interview_id).offset(skip).limit(limit).all()

def get_interview_answer_ners_for(answer_id: int, db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.InterviewAnswerNER).filter(models.InterviewAnswerNER.interview_answer_id == answer_id).offset(skip).limit(limit).all()