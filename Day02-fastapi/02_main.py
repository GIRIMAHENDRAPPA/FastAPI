from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: bool = True
    
@app.post("/blog")
def create_blog(request: Blog):
    return {"message": f"Blog '{request.title}' created","data": request}

#Day 02 - for your RAG project future
class QueryRequest(BaseModel):
    query: str
    
@app.post("/query")
def ask_question(req: QueryRequest):
    return {"answer": f"You asked: {req.query}","embedding_size":384}