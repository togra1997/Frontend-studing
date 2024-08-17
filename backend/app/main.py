from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Account(BaseModel):
    name: str
    initial_deposit: float

class Todo(BaseModel):
    task:str

@app.get("/hello")
def hello_world() -> dict[str, str]:
    return {"message": "Hello World"}

@app.post("/todo")
def test():
    return {"message": "Hello Python"}

@app.post('/account')
def create_account(account: Account):
    # ...ここで銀行口座を作成する処理をする...
    return {"account_number": "1234567890"}

# @app.get("/")
# def hello_world() -> dict[str, str]:
#     print("hello")
#     return {"message": "Hello World"}