**Important topics about Pytest Framework**

What is pytest?
Pytest is a test Engine or test framework in python

**TestFunction:**
Test function are executable function, after you write the piece of the code you can directly run them.
Like we define function, we can specify the test function by adding a "test_" keyword at the beginning or in the end.
And the same name needs to be used while saving the program.

Syntax:
def test_initialtest(): --> This will be treated as an automated test

**Fixtures:** We can mark the reusable code(pre-setup) under separate Fixture function
Syntax: @pytest.fixtures()

To link both, need to pass the function name as a parameter in the pytest function

Example:
@pytest.fixture
def prework():
    print("Browser Login Page")

def test_initial_test(prework):
    print("Testing Initial Test")

-> @pytest.fixtures(scope="function") :  It will run all the test at entire test level
-> @pytest.fixtures(scope="module") :  It will run the python file only one time irrespective of test
-> @pytest.fixtures(scope="class") : It is very similar to (scope="module"), when we have class defined we will use this method
-> @pytest.fixtures(scope="session") : It is similar to module, the python fixture will run once in the entire session
-> conftest.py : We can create a python fine in the same name and keep all the fixtures inside this, we can directly call the fixtures functions from here
--> We can return something in fixtures & that can be asserted in any of the test using assert keywork 
EG: assert postwork == "END"
--> With the help of "yield" keyword we can segregate the setup and teardown activity in the same fitures

**Useful GIT Commands**
--> pytest test_initialtest.py command will run the particular file
--> pytest test_initialtest.py::test_initialtest -s will help in running the particular test
--> @pytest.mark.skip will skill a particular method
--> @pytest.mark.smoke/regression -> We can tag a test using specific keywords and use them for execution using pytest -m smoke command

****Playwright Comments***

Official website: Syntax Link: https://playwright.dev/python/docs/locators#locate-by-text

Basic Code:
1. From playwright.sync_api import page     -> Will import the playwright package
2. Browser = Playwright.chromium.launch()   -> Launch the browser
3. Context = Browser.new_context()          -> Will set a new contex (Meaning, will not refer old cookies/cache)
4. Page = context.new_page()                -> Launch a new Page
5. Page.goto(Desired URL)                   -> Launch the URL

Basic Locators:
1. Page.get_by_label("label name").fill()   -> If label name available, please use. It must be a form type.
2. Page.get_by_role("combobox/alert/button/etc").select_option/click/press("actual option name") -> Safest way to locate particular field/element.
3. Page.locator(#id name).check/click()     -> It's called CSS selector. If ID name is available we can use it.
4. Page.locator(.classname).check/click()   -> If class name is available we can use this method. We can check the locator by using selectorhub
5. Page.locator(tagname).click              -> If there is a unique tag name, we can use this method.
6. page.get_by_text("I Agree").check()      -> If text is unique, we shall use this method.