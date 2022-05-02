from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'i am in login page with username & password')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given i am in login page with username & password')
driver = webdriver.Chrome(executable_path="C:\\Users\\basav\\Downloads\\seleniumdriver\\chromedriver.exe")
driver.get("https://demo.guru99.com/test/newtours/index.php")
@when(u'i enter "robert" and "robert"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When i enter "robert" and "robert"')


driver.find_element(by=By.NAME, value="userName").send_keys("user")
#      locate or identify password text box
driver.find_element(by=By.NAME, value="password").send_keys("pwd")

@when(u'click on submit')
def step_impl(context):
    raise NotImplementedError(u'STEP: When click on submit')
driver.find_element(by=By.NAME, value="submit").click()

@then(u'verify the title of the page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verify the title of the page')
print(driver.title)

@when(u'i enter "joel" and "joel"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When i enter "joel" and "joel"')
driver.find_element(by=By.NAME, value="userName").send_keys("user")
#     # locate or identify password text box
driver.find_element(by=By.NAME, value="password").send_keys("pwd")
