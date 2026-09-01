from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Task Management API"}


@app.get("/tasks")
def get_tasks():
    return {"tasks": []}