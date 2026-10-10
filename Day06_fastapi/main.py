from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
import models
import schemas
from database import engine, get_db
from typing import Optional

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Create User
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get Users with filter + pagination - DAY06 CONCEPT
@app.get("/users/", response_model=list[schemas.User])
def get_users(skip: int = 0, limit: int = 10, search: Optional[str] = Query(None), db: Session = Depends(get_db)):
    query = db.query(models.User)
    if search:
        query = query.filter(models.User.name.contains(search))
    return query.offset(skip).limit(limit).all()

# Update - NEW
@app.put("/users/{user_id}")
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    return db_user

# Delete - NEW
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "Deleted"}