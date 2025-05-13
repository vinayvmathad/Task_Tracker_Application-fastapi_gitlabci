from .models import Task
from sqlalchemy.orm import Session

def get_tasks(db: Session):
    return db.query(Task).all()

def create_task(db: Session, title: str):
    task = Task(title=title)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def complete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.completed = True
        db.commit()
    return task
