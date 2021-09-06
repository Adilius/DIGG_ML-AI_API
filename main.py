#I will now change this file by adding a comment // Björn

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World! /Laptop"}

