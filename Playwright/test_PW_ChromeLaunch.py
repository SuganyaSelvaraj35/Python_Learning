# For a customized requirement we can use this format

import time
from playwright.sync_api import Playwright
from playwright.sync_api import Page


def test_chromelaunch(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(no_viewport=True) # Maximize the chrome
    page = context.new_page()
    page.goto("https://practice.expandtesting.com/?utm_source=chatgpt.com")
    Page.get_by_role("link", name="Test Login Page").click()

# When the request is on single browser, headless=true(it will show the chrome launch), one context

def test_secondway(page: Page):
    page.goto("https://practice.expandtesting.com/?utm_source=chatgpt.com")
    page.get_by_role("link", name = "Test Login Page").click()
    time.sleep(3)
