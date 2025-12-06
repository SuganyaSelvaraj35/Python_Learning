import playwright

from playwright.sync_api import Page, expect


def test_handle_childwindow(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as new_pageInfo: # Opening child window
        page.locator(".blinkingText").click()
        child_page = new_pageInfo.value # Storing the new page value is child page object
        text = child_page.locator(".red").text_content()
        print(text)
        #Actual String: Please email us at mentor@rahulshettyacademy.com with below template to receive response
        trim_mail = text.split("at") #Splitting the string into 2 index which is before and after at
        email = trim_mail[1].strip().split(" with")[0] # Again splitting the result string into two part before and after with
        assert email == "mentor@rahulshettyacademy.com" #Pytest assertion to validate actual & expected


