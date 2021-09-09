from fastapi import FastAPI, Request
import requests

print("Hello I'm main.py running FastAPI")

app = FastAPI()

@app.on_event("startup")
async def startup():
    print('Starting up.....')

@app.on_event("shutdown")
async def startup():
    print('Shutting down.....')

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/api")
async def root(request: Request):
    api_url = request.headers.get('api_url')
    response = requests.get(api_url)
    response_body = response.json()
    return {"message": "Requesting from url: " + api_url,
            "response:": response_body}

