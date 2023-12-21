import allure
from allure_commons.types import AttachmentType
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
    context.browser.find_element(By.ID, 'email').send_keys(email.replace('"', ""))


@when(u'I enter {password} Password and Click Sign In')
def step_impl(context, password):
    context.browser.find_element(By.ID, 'pass').send_keys(password.replace('"', ""))
    context.browser.find_element(By.ID, 'send2').click()


@then(u'I should be logged in')
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=25, poll_frequency=1, ignored_exceptions=None)
    webElement = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Welcome, dono kasino!')]")))
    allure.attach(context.browser.get_screenshot_as_png(), name="login", attachment_type=AttachmentType.PNG)
    assert "Welcome" in webElement.text

@then(u'I still in Customer Login Page')
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=25, poll_frequency=1, ignored_exceptions=None)
    webElement = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Customer Login')]")))
    assert (webElement.text) == "Customer Login"


@then(u'Required Field Email message show up')
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=25, poll_frequency=1, ignored_exceptions=None)
    webElement = wait.until(EC.presence_of_element_located((By.ID, 'email-error')))
    assert (webElement.text) == "This is a required field."


@then(u'Required Field Password message show up')
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=25, poll_frequency=1, ignored_exceptions=None)
    webElement = wait.until(EC.presence_of_element_located((By.ID, 'pass-error')))
    assert (webElement.text) == "This is a required field."


@then(u'Error message show up')
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=25, poll_frequency=1, ignored_exceptions=None)
    webElement = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@data-ui-id, 'message-error')]")))
    assert (webElement.text) == "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."


@then(u'Please enter a valid email address Error show up')
def step_impl(context):
    wait = WebDriverWait(context.browser, timeout=25, poll_frequency=1, ignored_exceptions=None)
    webElement = wait.until(EC.presence_of_element_located((By.ID, 'email-error')))
    assert (webElement.text) == "Please enter a valid email address (Ex: johndoe@domain.com)."