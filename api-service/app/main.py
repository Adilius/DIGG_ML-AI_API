from fastapi import FastAPI
from app.router.api import api_router

description = """
Dataset Evaluator API helps you evaluate a dataset automatically! 🤖

## URL

Check if the URL to a dataset is able to be retrieved

## Parse

View the parsed dataset from the URL

## Eval

Evaluate the dataset parsed from the URL

"""

app = FastAPI(
    openapi_url="/openapi.json",
    description=description,
    docs_url="/docs",
    title='Dataset Evaluator')

@app.on_event("startup")
async def startup():
    print('Starting FastAPI up.....')

@app.on_event("shutdown")
async def startup():
    print('Shutting FastAPI down.....')

app.include_router(api_router)