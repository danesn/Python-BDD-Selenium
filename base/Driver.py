from selenium import webdriver
import utilities.CustomLogger as CL

class Driver:
    log = CL.customLogger()

    chromeDriverPath = "D:\Learn Automation Selenium\driver\chromedriver64\chromedriver.exe"
    firefoxDriverPath = None

    def getWebDriver(self, browser="chrome"):
        browserName = browser.lower()

        if browserName == 'chrome':
            driver = webdriver.Chrome(executable_path=self.chromeDriverPath)
            self.log.info("Chrome driver is initializing...")
        else:
            self.log.error("Browser Name is not Found!")