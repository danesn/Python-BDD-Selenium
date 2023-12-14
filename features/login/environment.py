from selenium import webdriver
import time

def before_scenario(context, scenario):
    context.browser = webdriver.Chrome("D:\Learn Automation Selenium\driver\chromedriver64\chromedriver.exe")
    context.browser.maximize_window()

def after_scenario(context, scenario):
    context.browser.quit()