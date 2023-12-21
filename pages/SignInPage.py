from base.BasePage import BasePage
import utilities.CustomLogger as CL

class SignInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators value in Sign In / Login Page
    _emailInput = 'email' # id
    _passwordInput = 'pass' # id
    _signInButton = 'send2' # id

    def enterEmail(self, email):
        self.sendTextToElement(email, 'id', self._emailInput)
        CL.allureLogs("Enter email")

    def enterPassword(self, password):
        self.sendTextToElement(password, 'id', self._passwordInput)
        CL.allureLogs("Enter password")

    def clickSignInButton(self):
        self.clickOnElement('id', self._signInButton)
        CL.allureLogs("Clicked sign in button")