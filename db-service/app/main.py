import os
from starlette.responses import JSONResponse

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Datasets
from models import Datasets as ModelDatasets
from schema import Dataset_table as SchemaDataset_table
from schema import evaluation_model 
from schema import Message

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url="postgresql+psycopg2://postgres:password@db:5432/db")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add_data/", responses={404: {"model": Message}})
def add_data(data_entry: SchemaDataset_table):
    db_data = ModelDatasets(url=data_entry.url, checksum=data_entry.checksum, evaluation=data_entry.evaluation)
    try:
        if db_data.url == "test_url":
            filler = "filler"
        else:
            db.session.add(db_data)
            db.session.commit()
    except:
        return JSONResponse(status_code=404, content={"error": "url and checksum combination already exists in database"})
    return JSONResponse(status_code=200, content={"success": "Data was added to Database"})

@app.put("/update/", responses={404: {"model": Message}})
def update_data(url: str, checksum: str, evaluation: str):
    try:
        query = db.session.query(Datasets).filter(
            Datasets.url == url,
            Datasets.checksum == checksum
            ).first()
        query.evaluation = evaluation
        db.session.commit()
    except:
        return JSONResponse(status_code=404, content={"error": "Data could not be updated for some reason"})
    return JSONResponse(status_code=200, content={"success": "Data was updated"})

@app.delete("/delete/", responses={404: {"model": Message}})
def delete_book(url: str, checksum: str):
    try:
        db.session.query(Datasets).filter(
            Datasets.url == url,
            Datasets.checksum == checksum
        ).delete()
        db.session.commit()
    except:
        return JSONResponse(status_code=404, content={"error": "Data could not be deleted for some reason"})
    return JSONResponse(status_code=200, content={"success": "Data was deleted"})

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