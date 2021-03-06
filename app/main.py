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

# Route - POST - Create new Case
@app.post("/cases/", response_model=schemas.Case)
def create_case(db: Session = Depends(get_db)):
    return crud.create_case(db=db)

# Route - GET - get all cases
@app.get("/cases/", response_model=schemas.Case)
def get_all_cases(db: Session = Depends(get_db)):
    return crud.get_all_cases(db=db)

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

# Route - POST - Create a license footage object and add plates for json object
@app.post("/licenses/", response_model=schemas.LicenseFootage)
def create_license_footage(license_footage: schemas.CreateLicenseFootageObj, db:Session = Depends(get_db)):
    return crud.create_license_footage_with_obj(license_footage=license_footage, db=db)

# Route - GET - get all the plates identified for a license_footage_id
@app.get("/licenses/{footage_id}/plates", response_model=List[schemas.RecognizedPlate])
def get_plates_for_footage_id(footage_id: int, skip: int = 0, limit: int= 100, db: Session = Depends(get_db)):
    plates = crud.get_license_plates_for_filename(footage_id=footage_id, skip=skip, limit=limit, db=db)
    return plates

@app.get("/licenses/plates/{license_plate_number}", response_model=List[schemas.LicenseFootage])
def get_footage_for_plate_id(license_plate_number: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    footage = crud.get_footage_for_plate_id(license_plate_number=license_plate_number, skip=skip, limit=limit, db=db)
    return footage

# Route - GET - get all blobs on server for case number
@app.get("/{case}/blobs", response_model=List[schemas.Blob])
def get_blobs_for_case(case: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cases = crud.get_all_blobs_for_case(case=case, skip=skip, limit=limit, db=db)
    return cases

# Route - POST - create blob with blobCreate and Case No.
@app.post("/{case}/blobs", response_model=schemas.Blob)
def create_blob_with(case: int, blob: schemas.CreateBlob, db: Session = Depends(get_db)):
    return crud.create_blob_with(db=db, case=case, blob=blob)

# Route - POST - create question with QuestionCreate and Case No.
@app.post("/{case}/questions", response_model=schemas.Question)
def create_question_with(case: int, question: schemas.CreateQuestion, db: Session = Depends(get_db)):
    return crud.create_question_with(db=db, case=case, question=question)

# Route - GET - get all cases for a specific Case No.
@app.get("/{case}/questions", response_model=List[schemas.Question])
def get_questions_for(case: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    questions = crud.get_questions_for(case=case, db=db, skip=skip, limit=limit)
    return questions

# Route - POST - Create Interview for Case No.
@app.post("/{case}/interviews", response_model=schemas.Interview)
def create_interview_with(case: int, interviewShell: schemas.CreateInterviewShell, db: Session = Depends(get_db)):
    return crud.create_interview_shell_for(case=case, db=db, interviewShell=interviewShell)

# Route - POST - Post data for Interview object
@app.post("/interviews/{interview_id}/data", response_model=schemas.Interview)
def post_data_for_interview_with(interview_id: int, interview: schemas.CreateInterview, db: Session = Depends(get_db)):
    return crud.post_data_for_interview_with(interview_id=interview_id, db=db, interview=interview)

# Route - GET - Get all interviews for a Case No.
@app.get("/{case}/interviews", response_model=List[schemas.Interview])
def get_interview_for(case: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return crud.get_interview_for(case=case, db=db, skip=skip, limit=limit)

# Route - GET - Get all interview answers for a Interview ID
@app.get("/interviews/{interview_id}/answers", response_model=List[schemas.InterviewAnswer])
def get_interview_answers_for(interview_id: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return crud.get_interview_answers_for(interview_id=interview_id, db=db, skip=skip, limit=limit)

# Route - GET Get all interview answer NERS for an Interview Answer ID
@app.get("/interviews/answers/{answer_id}/ners", response_model=List[schemas.InterviewAnswerNER])
def get_interview_answers_for(answer_id: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return crud.get_interview_answer_ners_for(answer_id=answer_id, db=db, skip=skip, limit=limit)