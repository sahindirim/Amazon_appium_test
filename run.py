import time
from appium import webdriver
from test_cases.Test_cases import Amazon_test
with Amazon_test as run_test:
    run_test.test_login()
    run_test.test_scenario_1()
    run_test.test_scenario_2()


