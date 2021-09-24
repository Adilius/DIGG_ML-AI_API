from fastapi import APIRouter
import requests
from ..algorithm import json_counter
from ..algorithm import main
from ..dependencies import data_handler
from ..dependencies import hash_handler
import json
from time import time
import httpx
import asyncio

api_router = APIRouter()

async def call_api():

    headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

    data = '{ "url": "------", "hash": "-------", "evaluation": "TEST" }'

    #r = await client.post('http://localhost:8002/add-data/', headers=headers, data=data)
    print("-------------------Tesst---------------------------")
    print("-------------------Tesst---------------------------")
    print("-------------------Tesst---------------------------")
    print("-------------------Tesst---------------------------")
    print("-------------------Tesst---------------------------")
                                

async def postDB(client, url: str, hash: str, evaluation: str):

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    
    data = {    "url": url,
                "hash": hash,
                "evaluation": "test"
    }
    
    data = '{ "url": "kalle", "hash": "pelle", "evaluation": "erik" }'

    try:
        response = await client.post('http://localhost:8002/add-data/', headers=headers, data=data)
        print(response)
    except:
        print('Failed to post to database')

    return "hello"

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
    hash = hash_handler.getHash(response)
    print(f"Hash: {hash}")

    # Get evaluation
    evaluation = main.evaluate_dataset(response)
    #evaluation_json = json.dumps(evaluation)

    # Post to DB
    #async with httpx.AsyncClient() as client:
    #    task = postDB(client, url, hash, evaluation)
    #    result = await asyncio.gather(task)

    
    print('-------------------Tesst---------------------------')
    call_api()
    

    return evaluation


