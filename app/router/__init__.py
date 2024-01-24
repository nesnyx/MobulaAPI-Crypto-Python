from fastapi import APIRouter, Request,Form,Query,HTTPException,status
from typing import Annotated
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.api import crypto
import requests

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def home(request:Request):
    return templates.TemplateResponse("home.html",{
        'request': request
    })

@router.get("/coins")
async def coins(request : Request ):
    return templates.TemplateResponse("coins.html",{
        "request" : request,
    
    })
@router.get("/coins/search")
async def getCoinsSearch(request : Request, coin:str = Annotated[Form(...), None]):
    headers ={
            'Content-Type' : "application/json",
            "Authorization" : "YOUR_API_KEY"
    }
    response = requests.get(f"https://api.mobula.io/api/1/market/data?asset={coin}", headers)
    data =response.json()
    return templates.TemplateResponse("get/getMarketData.html",{
            "request" : request,
            "data" : data,
            "price" : int(data['data']['price'])
        })


@router.get("/about")
async def market(request:Request):
    return templates.TemplateResponse("about.html",{
            "request" : request,
        })


@router.get("/contact")
async def market(request:Request):
    return templates.TemplateResponse("contact.html",{
            "request" : request,
        })