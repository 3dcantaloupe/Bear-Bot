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
    response = requests.get(endpt)
    response.raise_for_status()
    search_results = response.json()
    content_url = search_results[random.randint(0,30)]['download_url']
    return content_url
