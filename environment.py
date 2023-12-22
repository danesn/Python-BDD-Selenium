import allure
from selenium import webdriver
import time

def before_scenario(context, scenario):
    driverPath = "D:\Learn Automation Selenium\driver\chromedriver64\chromedriver.exe"
    context.driver = webdriver.Chrome(driverPath)
    context.driver.maximize_window()

def after_scenario(context, scenario):

    stdout = context.stdout_capture.getvalue()
    stderr = context.stderr_capture.getvalue()
    if stdout:
        allure.attach(stdout, name="stdout", attachment_type=allure.attachment_type.TEXT)
    if stderr:
        allure.attach(stderr, name="stderr", attachment_type=allure.attachment_type.TEXT)

    context.driver.quit()