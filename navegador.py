from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def criar_driver():
	driver = webdriver.Chrome()
	driver.maximize_window()
	return driver

def fechar_driver(driver):
	driver.quit()