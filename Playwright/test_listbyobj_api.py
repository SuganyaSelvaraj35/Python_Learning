import json

import requests
from playwright.sync_api import Playwright, sync_playwright #Import from playwright sync package

def test_listbyobj_api(): #Defining a function, test_ is automatically treated as a test case.
    with sync_playwright() as objapi:
        new_context = objapi.request.new_context() # creates a new API client for sending HTTP requests
        url = new_context.get("https://api.restful-api.dev/objects?id=3&id=5&id=10") #performs the API call.
        actual_response = url.json() #convert the API response into python format
        print(actual_response)

        with open(r"C:\API_Request folder\Listofobjects.txt", "r") as f: # Open the filein read mode
            response_content = json.load(f) #Parses JSON, It interprets the text as JSON format
            print(response_content)

            assert response_content == actual_response #COmpare the actual vs the expected




