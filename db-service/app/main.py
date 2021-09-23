import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Datasets
from models import Datasets as ModelDatasets
from schema import Dataset_table as SchemaDataset_table

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url="postgresql+psycopg2://postgres:password@db:5432/db")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add-data/", response_model=SchemaDataset_table)
def add_data(test: SchemaDataset_table):
    db_data = ModelDatasets(name=test.name, rating=test.rating, testProperty=test.testProperty)
    #db_data = ModelDatasets(name="Jonas", rating=5, testProperty="Winner")
    db.session.add(db_data)
    db.session.commit()
    return db_data

@app.get("/getdata/")
def get_data():
    StoredData = db.session.query(Datasets).all()

    return StoredData


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)