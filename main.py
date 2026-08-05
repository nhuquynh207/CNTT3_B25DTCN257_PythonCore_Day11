from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from routers.book_router import router 
from database import Base, engine, get_db


app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(router)
