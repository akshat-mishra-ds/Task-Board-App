from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# allow React to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks = []
task_id = 1


@app.get("/tasks/")
def get_tasks():
    return tasks


@app.post("/tasks/")
def add_task(task: dict):
    global task_id

    new_task = {
        "id": task_id,
        "taskname": task["taskname"],
        "complete": task["complete"]
    }

    tasks.append(new_task)
    task_id += 1

    return new_task


@app.delete("/tasks/{task_id}/")
def delete_task(task_id: int):
    global tasks

    tasks = [t for t in tasks if t["id"] != task_id]

    return {"message": "Task deleted"}