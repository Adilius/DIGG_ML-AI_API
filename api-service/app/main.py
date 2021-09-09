from fastapi import FastAPI, Request
import requests

from app.api.dataset import dataset

print("Hello I'm main.py running FastAPI")

app = FastAPI(openapi_url="/api/openapi.json", docs_url="/api/docs")

@app.on_event("startup")
async def startup():
    print('Starting up.....')

@app.on_event("shutdown")
async def startup():
    print('Shutting down.....')

app.include_router(dataset, prefix='/api/dataset', tags=['dataset'])