from traceback import print_stack

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import utilities.CustomLogger as CL

class BasePage:

    log = CL.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def launchWebPage(self, url, title):
        try:
            self.driver.get(url)
            assert self.driver.title == title

            # Logging
            self.log.info("Web Page Launch with URL : " + url)
            print("Web Page Launch with URL : " + url)

        except:

            # Logging
            self.log.error("Web Page not Launch with URL : " + url)
            print("Web Page not Launch with URL : " + url)
            print_stack()

    def getLocatorType(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "plink":
            return By.PARTIAL_LINK_TEXT
        elif locatorType == "tag":
            return By.TAG_NAME
        else:
            self.log.error("LocatorType : " + locatorType + "is not Found!")
            print("LocatorType : " + locatorType + "is not Found!")

        return False

    def getWebElement(self, locatorType, locatorValue):
        webElement = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)

            webElement = self.driver.find_element(locatorByType, locatorValue)

            # Log
            self.log.info("WebElement found with LocatorValue " + locatorValue + " using LocatorType " + locatorType)
            print("WebElement found with LocatorValue " + locatorValue + " using LocatorType " + locatorType)

        except:
            # Log
            self.log.error("WebElement not found with LocatorValue " + locatorValue + " using LocatorType " + locatorType)
            print("WebElement not found with LocatorValue " + locatorValue + " using LocatorType " + locatorType)
            print_stack()

            assert False

        return webElement

    def waitForElement(self, locatorType, locatorValue):
        webElement = None
        try :
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)

            wait = WebDriverWait(self.driver, timeout=25, poll_frequency=1, ignored_exceptions=None)
            webElement = wait.until(EC.presence_of_element_located((locatorByType, locatorValue)))

            # Log
            self.log.info("WebElement found with LocatorValue " + locatorValue + " using LocatorType " + locatorType)
            print("WebElement found with LocatorValue " + locatorValue + " using LocatorType " + locatorType)

        except:
            # Log
            self.log.error("WebElement not found with LocatorValue " + locatorValue + " using LocatorType " + locatorType)
            print("WebElement not found with LocatorValue " + locatorValue + " using LocatorType " + locatorType)
            print_stack()

            assert False

        return webElement

    def clickOnElement(self, locatorType, locatorValue):
        webElement = None
        try:
            webElement = self.waitForElement(locatorType, locatorValue)
            webElement.click()

            # Log
            self.log.info("Clicked on WebElement with LocatorValue " + locatorValue + " using LocatorType " + locatorType)
            print("Clicked on WebElement with LocatorValue " + locatorValue + " using LocatorType " + locatorType)

        except:
            # Log
            self.log.error("Unable to Click WebElement with LocatorValue " + locatorValue + " using LocatorType " + locatorType)
            print("Unable to Click WebElement with LocatorValue " + locatorValue + " using LocatorType " + locatorType)
            print_stack()

            assert False

    def sendTextToElement(self, text, locatorType, locatorValue):
        webElement = None
        try:
            webElement = self.waitForElement(locatorType, locatorValue)
            webElement.send_keys(text)

            # Log
            self.log.info("Send the text '" + text + "' with LocatorValue " + locatorValue + " using LocatorType " + locatorType)
            print("Send the text '" + text + "' with LocatorValue " + locatorValue + " using LocatorType " + locatorValue)

        except:
            # Log
            self.log.error("Unable to Send the text '" + text + "' with LocatorValue " + locatorValue + " using LocatorType " + locatorType)
            print("Unable to Send the text '" + text + "' with LocatorValue " + locatorValue + " using LocatorType " + locatorType)
            print_stack()

            assert False

    def getTextElement(self, locatorType, locatorValue):
        text = None
        try:
            webElement = self.waitForElement(locatorType, locatorValue)
            text = webElement.text

            # Log
            self.log.info("Get the Text '" + text + "' with LocatorValue " + locatorValue + " LocatorType " + locatorType)
            print("Get the Text '" + text + "' with LocatorValue " + locatorValue + " LocatorType " + locatorType)

        except:
            # Log
            self.log.error("Unable to Get the text with LocatorValue " + locatorValue + " using LocatorType " + locatorType)
            print("Unable to Get the text with LocatorValue " + locatorValue + " using LocatorType " + locatorType)
            print_stack()

            # Take screenshot
            self.takeScreenshot(locatorType)
            assert False

        return text

    def isElementDisplayed(self, locatorType, locatorValue):
        webElement = None
        isDisplayed = None
        try:
            webElement = self.waitForElement(locatorType, locatorValue)
            isDisplayed = webElement.is_displayed()

            # Log
            self.log.info("WebElement is Displayed on WebPage with LocatorValue " + locatorValue + " using LocatorType " + locatorType)
            print("WebElement is Displayed on WebPage with LocatorValue " + locatorValue + " using LocatorType " + locatorType)

        except:
            # Log
            self.log.error("WebElement is not Displayed on WebPage with LocatorValue " + locatorValue + " using LocatorType " + locatorType)
            print("WebElement is not Displayed on WebPage with LocatorValue " + locatorValue + " using LocatorType " + locatorType)
            print_stack()

            assert False

        return isDisplayed

    def moveToElement(self, locatorType, locatorValue): # we can use this for scrolling to the element as well
        webElement = None
        actions = ActionChains(self.driver)

        try:
            webElement = self.waitForElement(locatorType, locatorValue)
            actions.move_to_element(webElement)
            actions.perform()
            self.log.info("Move to WebElement on Page with LocatorType " + locatorType + " using LocatorValue " + locatorValue)
        except:
            self.log.error("Unable to Move to WebElement on Page with LocatorType " + locatorType + " using LocatorValue " + locatorValue)
            print_stack()
            assert False

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)