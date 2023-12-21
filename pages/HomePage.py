from selenium import webdriver

from base.BasePage import BasePage
import utilities.CustomLogger as CL

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators value in HomePage
    _signInPage = "Sign In" # link

    def launchHomePage(self):
        self.launchWebPage("https://magento.softwaretestingboard.com/", title="Home Page")
        CL.allureLogs("Launch Home page")

    def clickSignIn(self):
        self.clickOnElement('link', self._signInPage)
        CL.allureLogs("Click Sign in Link")