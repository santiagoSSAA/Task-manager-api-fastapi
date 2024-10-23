from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import task as task_crud
from app.schemas.task import Task, TaskCreate
from app.db.database import get_db

router = APIRouter()

@router.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return task_crud.create_task(db=db, task=task)

@router.get("/tasks/", response_model=list[Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = task_crud.get_tasks(db, skip=skip, limit=limit)
    return tasks

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted = task_crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}

