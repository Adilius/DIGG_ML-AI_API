from fastapi import APIRouter
import requests

api_router = APIRouter()

@api_router.get('/')
async def root():
    return {"message": "Hello World!"}

@api_router.get("/url/")
async def root(url: str):
    print('Incoming request')
    print(f'url = {url}')
    try:
        response = requests.get(url)
        response_body = response.json()
    except:
        return {"message": "Could not read API url"}
    else:
        return  {"Request URL": url,
                "response:": response_body
                }