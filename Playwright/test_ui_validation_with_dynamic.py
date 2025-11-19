import time
from playwright.sync_api import Page, expect


def test_UIValidation_with_dynamic(page: Page):
    page.goto("https://www.flipkart.com/")
    page.locator(".Pke_EE").fill("Apple 17 pro")
    page.locator(".Pke_EE").press("Enter")

    # NEW TAB handling
    with page.context.expect_page() as new_page_info:
         page.locator("//div[normalize-space()='Apple iPhone 17 Pro (Deep Blue, 256 GB)']").click()
    new_page = new_page_info.value

    #Exclude buttons that have the disabled attribute and find the actual button
    new_page.locator("button:has-text('Add to cart'):not([disabled])").click()


    time.sleep(2)