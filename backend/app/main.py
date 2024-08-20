from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, field_validator

task_count = 0


class Task(BaseModel):
    task: str
    id: int = Field(None, validate_default=True)

    @field_validator("id", mode="before")
    def set_id_based_on_count(cls: "Task", v: int) -> int:
        global task_count
        task_count += 1
        return task_count


app = FastAPI()

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
)

todo_list: list[Task] = []


@app.get("/todo")
async def todo() -> list[Task]:
    print("test")
    print(todo_list)
    return todo_list


@app.post("/todo")
async def add(req: Task) -> Task:
    print(f"{req}")
    todo_list.append(req)
    return req


@app.delete("/todo/{task_id}")
async def delete(task_id: int) -> None:
    for task in todo_list:
        if task.id == task_id:
            todo_list.remove(task)


@app.exception_handler(RequestValidationError)
async def handler(request: Request, exc: RequestValidationError):
    print(exc)
    return JSONResponse(content={}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
