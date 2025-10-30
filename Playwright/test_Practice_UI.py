import pytest
from playwright.sync_api import Playwright
from playwright.sync_api import Playwright, expect, Page

def test_chrome_login(page: Page):

    page.goto("https://practice.expandtesting.com/?utm_source=chatgpt.com")
    page.get_by_role("link", name="Test Login Page").click()
    page.get_by_label("username").fill("practice")
    page.get_by_label("password").fill("SuperSecretPassword!")
    page.get_by_role("button", name = "Login").click()
    expect(page.get_by_text("Secure Area page for Automation Testing Practice")).to_be_visible()

def test_firefox_login(fpage: Page):

    fpage.goto("https://practice.expandtesting.com/?utm_source=chatgpt.com")
    fpage.get_by_role("link", name="Test Login Page").click()
    fpage.get_by_label("username").fill("practice")
    fpage.get_by_label("password").fill("SuperSecretPassword!")
    fpage.get_by_role("button", name = "Login").click()
    expect(fpage.get_by_text("Secure Area page for Automation Testing Practice")).to_be_visible()