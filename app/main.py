from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from . import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tasks/")
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@app.post("/tasks/")
def add_task(title: str, db: Session = Depends(get_db)):
    return crud.create_task(db, title)

@app.put("/tasks/{task_id}")
def mark_done(task_id: int, db: Session = Depends(get_db)):
    return crud.complete_task(db, task_id)
