import os

import uvicorn
from dotenv import load_dotenv
from fastapi import APIRouter
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Datasets
from models import Datasets as ModelDatasets
from schema import Dataset_table as SchemaDataset_table

api_router = APIRouter()

api_router.add_middleware(DBSessionMiddleware, db_url=os.environ["postgresql+psycopg2://postgres:password@db:5432/db"])

@api_router.get("/")
async def root():
    return {"message": "Hello World"}

@api_router.post("/add-data/", response_model=SchemaDataset_table)
def add_data(test: SchemaDataset_table):
    #db_data = ModelDatasets(name=test.name, rating=test.rating, testProperty=test.testProperty)
    db_data = ModelDatasets("Jonas", 5, "Winner")
    db.session.add(db_data)
    db.session.commit()
    return db_data

@api_router.get("/getdata/")
def get_books():
    StoredData = db.session.query(Datasets).all()

    return StoredData