from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'I am on the homepage')
def step_impl(context):
    context.browser.get("https://magento.softwaretestingboard.com/")
    assert (context.browser.title) == "Home Page"


@when(u'I click Sign In')
def step_impl(context):
    context.browser.find_element(By.LINK_TEXT, 'Sign In').click()


@then(u'Sign In page opens')
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=25, poll_frequency=1, ignored_exceptions=None)
    webElement = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Customer Login')]")))
    assert (webElement.text) == "Customer Login"


@when(u'I enter {email} Email')
def step_impl(context, email):
    context.browser.find_element(By.ID, 'email').send_keys(email)


@when(u'I enter {password} Password and Click Sign In')
def step_impl(context, password):
    context.browser.find_element(By.ID, 'pass').send_keys(password)
    context.browser.find_element(By.ID, 'send2').click()


@then(u'I should be logged in')
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=25, poll_frequency=1, ignored_exceptions=None)
    webElement = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'logged-in')))
    assert "Welcome" in webElement.text