from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Task(BaseModel):
    id:int
    title:str
    content:str
    is_done: bool

Tasks=[
    Task(id=1,title="home",content="i go to school everyday ",is_done=False),
    Task(id=2, title="school",content="I study every day",is_done=False)
]

@app.get("/tasks/")
async def get_tasks():
    return Tasks

@app.post("/tasks/")
async def add_task(Task: Task):
    Tasks.append(Task)
    return Task

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, updated_task:Task):
    for index , Tasked in enumerate(Tasks):
        if Tasked.id == task_id:
            Tasks[index]=updated_task
            return Tasks[index]
    return{"error, task not found"}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for index , task in enumerate(Tasks):
        if task.id== task_id:
            del Tasks[index]
            return{"task is delete"}
    return {"error: task not found"}
