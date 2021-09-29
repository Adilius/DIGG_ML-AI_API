from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests

test_router = APIRouter()

@test_router.get('/404/')
async def root():
    return JSONResponse(status_code=404)