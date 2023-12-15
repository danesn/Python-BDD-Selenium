from selenium import webdriver
import time

def before_scenario(context, scenario):
    driverPath = "D:\Learn Automation Selenium\driver\chromedriver64\chromedriver.exe"
    context.browser = webdriver.Chrome(driverPath)
    context.browser.maximize_window()

def after_scenario(context, scenario):
    context.browser.quit()