from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"data": "Hello World"}

@app.get("/about")
def about():
    return {"data": "Welcome to about page"}

@app.get("/name/{name}")
def home(name: str):
    return {"data": name}