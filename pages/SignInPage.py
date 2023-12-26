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
    _textCustomerLogin = "//span[contains(text(), 'Customer Login')]" # xpath
    _textWelcomingUser = "//span[contains(text(), 'Welcome, dono kasino!')]" # xpath
    _requiredEmailMessage = 'email-error' # id
    _requiredPasswordMessage = 'pass-error' # id
    _errorPasswordMessage = "//div[contains(@data-ui-id, 'message-error')]" # xpath

    def enterEmail(self, email):
        self.sendTextToElement(email, 'id', self._emailInput)
        CL.allureLogs("Enter email")

    def enterPassword(self, password):
        self.sendTextToElement(password, 'id', self._passwordInput)
        CL.allureLogs("Enter password")

    def clickSignInButton(self):
        self.clickOnElement('id', self._signInButton)
        CL.allureLogs("Clicked sign in button")

    def verifySignInPageOpen(self):
        text = self.getTextElement('xpath', self._textCustomerLogin)

        assert text == "Customer Login"
        CL.allureLogs('Verify sign in page open with "Customer Login" text')

    def verifySignInSuccessful(self):
        verifyWelcomingText = self.getTextElement('xpath', self._textWelcomingUser)
        self.takeScreenshot("verifySignInSuccessful")

        assert "Welcome" in verifyWelcomingText
        CL.allureLogs("Verify sign in successful")

    def checkIfRequiredEmailMessageShowup(self):
        elementDisplay = self.isElementDisplayed('id', self._requiredEmailMessage)
        assert elementDisplay == True

        if elementDisplay == True:
            elementText = self.getTextElement('id', self._requiredEmailMessage)
            assert elementText == "This is a required field."

    def checkIfRequiredPasswordMessageShowup(self):
        elementDisplay = self.isElementDisplayed('id', self._requiredPasswordMessage)
        assert elementDisplay == True

        if elementDisplay == True:
            elementText = self.getTextElement('id', self._requiredPasswordMessage)
            assert elementText == "This is a required field."

    def checkIfPasswordMessageShowup(self):
        elementDisplay = self.isElementDisplayed('xpath', self._errorPasswordMessage)
        assert elementDisplay == True

        if elementDisplay == True:
            elementText = self.getTextElement('xpath', self._errorPasswordMessage)
            assert elementText == "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."

    def checkIfEnterValidEmailMessageShowup(self):
        elementDisplay = self.isElementDisplayed('id', self._requiredEmailMessage)
        assert elementDisplay == True

        if elementDisplay == True:
            elementText = self.getTextElement('id', self._requiredEmailMessage)
            assert elementText == "Please enter a valid email address (Ex: johndoe@domain.com)."