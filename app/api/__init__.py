import requests
import os

from dotenv import load_dotenv
load_dotenv()

API_KEY= os.getenv("API_KEY")

class Crypto:
    def __init__(self,api) -> None:
        self.api = api
    def cryptocurrencies(self,url,asset:str):
        headers ={
            'Content-Type' : "application/json",
            "Authorization" : self.api
        }
        response = requests.get(f"{url}?asset={asset}", headers )
        data =response.json()
        return data
    
crypto = Crypto(API_KEY)