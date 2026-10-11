from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, SessionLocal, get_db, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/blogs")
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blogs")
def get_blogs(db: Session = Depends(get_db)):
    return db.query(models.Blog).all()