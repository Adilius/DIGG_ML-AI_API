from fastapi import APIRouter
import requests
from ..dependencies import data_handler

api_router = APIRouter()

@api_router.get('/')
async def root():
    return {"message": "Hello World!"}

@api_router.get("/url/")
async def root(url: str):
    print('Incoming url request')
    print(f'url = {url}')
    response = data_handler.validateURL(url)
    return response