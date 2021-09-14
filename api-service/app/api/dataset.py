from fastapi import APIRouter, HTTPException, Request
import requests

dataset = APIRouter()



#try this link
#http://localhost:8080/api/dataset/url/?url=https://opendata.umea.se/api/v2/catalog/datasets/skyddade-omraden-djur-och-vaxtskyddsomraden-sverigesweden/records
@dataset.get("/url/")
async def root(url: str):
    print(f'url = {url}')
    try:
        response = requests.get(url)
        response_body = response.json()
    except:
        return {"message": "Could not read API url"}
    else:
        return  {"message": f"Requesting from url: {url}",
                "response:": response_body
                }