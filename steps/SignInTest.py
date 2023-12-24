import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.HomePage import HomePage
from pages.SignInPage import SignInPage

class SignInTest:

    @given(u'I am on the homepage')
    def step_impl(context):

        # Make object class for pages
        context.homepage = HomePage(context.driver)
        context.signinpage = SignInPage(context.driver)

        # Launch Web browser to the Homepage
        context.homepage.clearAppendLog()  # Clear Log
        context.homepage.launchHomePage()
        context.homepage.appendLog()  # Print Log


    @when(u'I click Sign In')
    def step_impl(context):
        context.homepage.clearAppendLog()  # Clear Log
        context.homepage.clickSignIn()
        context.homepage.appendLog()  # Print Log


    @then(u'Sign In page opens')
    def step_impl(context):
        context.signinpage.clearAppendLog()  # Clear Log
        context.signinpage.verifySignInPageOpen()
        context.signinpage.appendLog()  # Print Log


    @when(u'I enter {email} Email')
    def step_impl(context, email):
        email = email.replace('"', "")
        context.signinpage.clearAppendLog() # Clear Log
        context.signinpage.enterEmail(email)
        context.signinpage.appendLog() # Print Log


    @when(u'I enter {password} Password and Click Sign In')
    def step_impl(context, password):
        password = password.replace('"', "")
        context.signinpage.clearAppendLog() # Clear Log
        context.signinpage.enterPassword(password)
        context.signinpage.clickSignInButton()
        context.signinpage.appendLog() # Print Log


    @then(u'I should be logged in')
    def step_impl(context):
        context.signinpage.clearAppendLog()  # Clear Log
        context.signinpage.verifySignInSuccessful()
        context.signinpage.appendLog()  # Print Log


    # @then(u'I still in Customer Login Page')
    # def step_impl(context):
    #     wait = WebDriverWait(context.browser, timeout=25, poll_frequency=1, ignored_exceptions=None)
    #     webElement = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Customer Login')]")))
    #     assert (webElement.text) == "Customer Login"
    #
    #
    # @then(u'Required Field Email message show up')
    # def step_impl(context):
    #     wait = WebDriverWait(context.browser, timeout=25, poll_frequency=1, ignored_exceptions=None)
    #     webElement = wait.until(EC.presence_of_element_located((By.ID, 'email-error')))
    #     assert (webElement.text) == "This is a required field."
    #
    #
    # @then(u'Required Field Password message show up')
    # def step_impl(context):
    #     wait = WebDriverWait(context.browser, timeout=25, poll_frequency=1, ignored_exceptions=None)
    #     webElement = wait.until(EC.presence_of_element_located((By.ID, 'pass-error')))
    #     assert (webElement.text) == "This is a required field."
    #
    #
    # @then(u'Error message show up')
    # def step_impl(context):
    #     wait = WebDriverWait(context.browser, timeout=25, poll_frequency=1, ignored_exceptions=None)
    #     webElement = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@data-ui-id, 'message-error')]")))
    #     assert (webElement.text) == "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."
    #
    #
    # @then(u'Please enter a valid email address Error show up')
    # def step_impl(context):
    #     wait = WebDriverWait(context.browser, timeout=25, poll_frequency=1, ignored_exceptions=None)
    #     webElement = wait.until(EC.presence_of_element_located((By.ID, 'email-error')))
    #     assert (webElement.text) == "Please enter a valid email address (Ex: johndoe@domain.com)."