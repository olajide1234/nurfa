from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from mangum import Mangum

from nurfa.v1 import router as v1

stage = os.environ.get('STAGE', 'dev')


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1.router)

@app.get("/")
def index():
    return {"Hello": "World"}


@app.get("/users/{user_id}")
def read_item(user_id: int):
    return {"user_id": user_id}

handler = Mangum(app)
