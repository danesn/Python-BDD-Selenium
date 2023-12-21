from selenium import webdriver
from selenium.webdriver.common.by import By

import  utilities.CustomLogger as CL

class BasePage:

    log = CL.customLogger()

    # Debug purpose
    debugDriver = webdriver.Chrome(executable_path="test")
    debugDriver.get("URL")
    a = debugDriver.title
    debugDriver.find_element(By.ID, "lala")

    def __init__(self, driver):
        self.driver = driver

    def launchWebPage(self, url, title):
        try:
            self.driver.get(url)
            assert self.driver.title == title
            self.log.info("Web Page Launch with URL : " + url)
        except:
            self.log.error("Web Page not Launch with URL : " + url)

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

        return False