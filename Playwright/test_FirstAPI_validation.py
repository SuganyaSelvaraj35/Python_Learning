from playwright.sync_api import sync_playwright #Importing playwright from sync package

def test_firstAPI(): # Defining function
    with sync_playwright() as p:
        context = p.request.new_context(extra_http_headers={"accept": "application/json"}) # Very first step would be defining a new context
        response = context.get("https://practice.expandtesting.com/notes/api/health-check") # access get method API
        print(response.json()) # Printing json response body
        assert response.ok
        assert response.status == 200

