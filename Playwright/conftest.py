# This file has to be present inside the same directory

import pytest
from playwright.sync_api import Playwright #we can access the playwright package

# Reusable function

@pytest.fixture(scope='session') # Syntax for fixture
def prework(): # define the function
    print("Browser Login Page")
    yield # tear down
    print("Everything done")

@pytest.fixture(scope='session')
def postwork():
    print("Browser logout Page")
    return "END"

@pytest.fixture(scope='function') # Syntax
def page(playwright): # Defining the function & calling playwright package
    chrome = playwright.chromium.launch(headless=False) # Launch crome browser
    context = chrome.new_context(viewport=None) # open up a fresh browser with its own cookies & session
    page = context.new_page() # Open the new tab, syntax is same for all the functions
    yield page # tear down activity
    context.close() # Close the tab
    chrome.close() # Close the browser

#Similar to chrome, but in firefox

@pytest.fixture(scope='function') # fixture syntax

# def fpage(playwright: Playwright): playwright is an object provided automatically by pytest-playwright — it’s your “remote control” for browsers.
#The type hint Playwright just helps explain that playwright belongs to Playwright’s library (It’s not mandatory, but good for clarity.)

def fpage(playwright: Playwright):
    f_fox = playwright.firefox.launch(headless=False) #launching the Firefox browser.
    context = f_fox.new_context(viewport=None) #new Firefox profile with full window size
    fpage = context.new_page() #opening one new tab (page).
    yield fpage #This line pauses the fixture and gives the page to your test
    context.close() # Close the tab
    f_fox.close() # Close the browser