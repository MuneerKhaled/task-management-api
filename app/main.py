from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Task Management API"}


tasks = []


@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}


@app.post("/tasks")
def create_task(task: dict):
    tasks.append(task)
    return {"message": "Task created", "task": task}