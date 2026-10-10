from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home():
    return {"message":"Day01 FastAPI running!"}

@app.get("/hello/{name}")
def hello(name:str):
    return {"Hello":name}

@app.get("/blog")
def blog(limit: int = 10, published: bool = True):
    if published:
        return {"data": f"{limit} published blogs"}
    else:
        return {"data": f"{limit} blogs"}