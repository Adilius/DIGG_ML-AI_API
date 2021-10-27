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
    print(f'Incoming url request:\n{url}')

    # Run checks
    response = data_handler.get_data(url)

    #print('response', response)
    #If we got error
    if 'Error' in response:
        return response
    else:
        return {
            "Success": "URL valid"
        }

@api_router.get("/parse/")
async def parse(url: str):
    print(f'Incoming parse request:\n{url}')

    # Run checks
    response = data_handler.get_data(url)

    return response


@api_router.get("/eval/")
async def eval(url: str):
    print(f'Incoming eval request: {url}')
    response = data_handler.get_data(url)

    #If we got error
    if 'Error' in response:
        return response

    # Get the checksum - depricated
    #checksum = checksum_handler.get_checksum(response)

    # Check database first
    print('Checking database:', end=" ")
    database_response = database_handler.get_result(url)
    if 'Error' in database_response:
        print(next(iter(database_response.values())))
    else:
        print('Retrieved stored results')
        return database_response
        

    # Get evaluation
    print('Creating new evaluation...', end=" ")
    #evaluation = main.evaluate_dataset(response)
    try:
        #pass
        evaluation = main.evaluate_dataset(response)
    except:
        print('Failed')
        return {
            'Error':'Evaluation failed'
        }
    print('Success')
    # Store in 
    
    try:
        response = database_handler.store_result(url, evaluation)
        #response = database_handler.store_result(url, evaluation)
        print('Successfully posted results to database')
    except:
        print('Failed to post result to database')

    return evaluation