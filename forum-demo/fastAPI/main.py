from typing import Annotated
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from db import models
from db.database import engine, get_db
from sqlalchemy.orm import Session
from routers import user


app = FastAPI()
app.include_router(user.router)

models.Base.metadata.create_all(bind=engine)
db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/")
async def root():
    return {"message": "Hello World"}
