from fastapi import APIRouter
import requests
from ..algorithm import main
from ..dependencies import data_handler
from ..dependencies import checksum_handler
from ..dependencies import database_handler

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

    # Get the checksum
    checksum = checksum_handler.get_checksum(response)

    # Get evaluation
    evaluation = main.evaluate_dataset(response)

    # Store in database
    try:
        response = database_handler.store_result(url, checksum, evaluation)
        print(response)
    except:
        print('Failed to post result to database')

    return evaluation