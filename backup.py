import os
import discord
from azure.cognitiveservices.search.imagesearch import ImageSearchClient
from msrest.authentication import CognitiveServicesCredentials
import json
import os 
from pprint import pprint
import requests
import random
from dotenv import load_dotenv

load_dotenv()

endpt = "https://picsum.photos/v2/list"

def backup(search_term):
    response = requests.get(endpt + '?page=' + str(random.randint(1,1000)) + '&limit=1')
    # response = requests.get(endpt + '?page=' + str(1000) + '&limit=1')
    response.raise_for_status()
    search_results = response.json()
    # print(search_results)
    if len(search_results)==0:
        return(backup(search_term))
    content_url = search_results[0]['download_url']
    return content_url
