from fastapi import APIRouter
import requests
from ..algorithm import main
from ..dependencies import data_handler
from ..dependencies import checksum_handler
from ..dependencies import database_handler

api_router = APIRouter()

@api_router.get('/')
async def root():
    return {"Success": "Hello World!"}

@api_router.get("/url/")
async def url(url: str):
    print('Incoming url request')
    print(f'url = {url}')

    # Run checks
    response = data_handler.get_data(url)

    print('response', response)
    #If we got error
    if 'Error' in response:
        return response
    else:
        return {
            "Success": "URL valid"
        }


@api_router.get("/eval/")
async def eval(url: str):
    print('Incoming eval request')
    print(f'url = {url}')
    response = data_handler.get_data(url)

    #If we got error
    if 'Error' in response:
        return response

    # Get the checksum
    checksum = checksum_handler.get_checksum(response)

    # Check database first
    database_response = database_handler.get_result(url, checksum)

    if 'Error' in database_response:
        print(database_response)
        print('No stored results found')
    else:
        print('Retrieved stored results')
        return database_response
        

    # Get evaluation
    print('Creating new evaluation...')
    evaluation = main.evaluate_dataset(response)

    # Store in database
    try:
        response = database_handler.store_result(url, checksum, evaluation)
        print(response)
        print('Successfully posted results to database')
    except:
        print('Failed to post result to database')

    return evaluation