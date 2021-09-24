from fastapi import APIRouter
import requests
from ..algorithm import json_counter
from ..algorithm import main
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


@api_router.get("/eval/")
async def root(url: str):
    print('Incoming eval request')
    print(f'url = {url}')
    response = data_handler.validateURL(url)

    #If we got error
    if next(iter(response)) == 'Error':
        return response

    
    # Get the hash

    res = main.evaluate_dataset(response)
    return res
