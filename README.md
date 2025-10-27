Pytest is a test Engine or test framework in python

Syntax: 

Like we define function, we can specify the test function by adding a keyword at the beginning or in the end

Eg : def test_initialtest(): --> Will be treated as an automated test

-> Fixtures: We can mark the reusable code(pre-setup) under Fixture function  

Syntax: @pytest.fixtures()

-> To link both, need to pass the function name as a parameter in the pytest function

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

--> pytest test_initialtest.py command will run the particular file


--> pytest test_initialtest.py::test_initialtest -s will help in running the particular test

--> @pytest.mark.skip will skill a particular method

-->  @pytest.mark.smoke/regression -> We can tag a test using specific keywords and use them for execution using pytest -m smoke command


<img width="1151" height="1683" alt="image" src="https://github.com/user-attachments/assets/d1d737e8-cac8-4617-8b12-acfc36f53493" />
