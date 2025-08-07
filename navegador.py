from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def criar_driver():

# Aqui pode usar Chrome, Firefox, etc

driver = webdriver.Chrome()

driver.maximize_window()

return driver

def fechar_driver(driver):

driver.quit()