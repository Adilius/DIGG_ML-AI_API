from fastapi import FastAPI, Request
import requests

from app.api.dataset import dataset

print("Hello I'm main.py running FastAPI")

app = FastAPI(openapi_url="/api/openapi.json", docs_url="/api/docs")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/LOL/")
async def root():
    return {"message": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}

@app.on_event("startup")
async def startup():
    print('Starting up.....')

@app.on_event("shutdown")
async def startup():
    print('Shutting down.....')

app.include_router(dataset, prefix='/api/dataset', tags=['dataset'])