from fastapi import APIRouter, HTTPException, Request
import requests

dataset = APIRouter()

@dataset.get('/')
async def root():
    return {"message": "Hello World!"}

@dataset.get("/api")
async def root(url: str):
    print(f'url = {url}')
    response = requests.get(url)
    response_body = response.json()
    return  {"message": "Requesting from url: ",
            "response:": response_body
            }