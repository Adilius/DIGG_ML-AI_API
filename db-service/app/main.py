import os
from starlette.responses import JSONResponse

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Datasets
from models import Datasets as ModelDatasets
from schema import Dataset_table as SchemaDataset_table
from schema import Dataset_table as DatarowIdentifier
from schema import Dataset_table as evaluation_model
from schema import Dataset_table as Message

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url="postgresql+psycopg2://postgres:password@db:5432/db")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add_data/", response_model=SchemaDataset_table, responses={404: {"model": Message}})
def add_data(data_entry: SchemaDataset_table):
    db_data = ModelDatasets(url=data_entry.url, checksum=data_entry.checksum, evaluation=data_entry.evaluation)
    try:
        db.session.add(db_data)
        db.session.commit()
    except:
        return JSONResponse(status_code=404, content={"error": "url and checksum combination already exists in database"})
    return db_data

@app.get("/get_data/", response_model = evaluation_model)
def get_data(url: str, checksum: str):
    query = db.session.query(Datasets).filter(
        Datasets.url == url,
        Datasets.checksum == checksum
    ).first()

    return query


@app.get("/get_all_data/")
def get_all_data():
    StoredData = db.session.query(Datasets).all()

    return StoredData


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)