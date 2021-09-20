from fastapi import FastAPI
from app.router.api import api_router

app = FastAPI(openapi_url="/openapi.json", docs_url="/docs")

@app.on_event("startup")
async def startup():
    print('Starting up.....')

@app.on_event("shutdown")
async def startup():
    print('Shutting down.....')

app.include_router(api_router, prefix='/api', tags=['api'])