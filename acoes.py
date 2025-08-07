from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select

from selenium.webdriver.support import expected_conditions as EC

from seletores import *

def esperareclicar(driver, by, seletor, timeout=10):
	elemento = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, seletor)))
	elemento.click()
	return elemento

def clicar_aba(driver, nome):
	caminho = XPATH_ABA.format(nome)
	esperareclicar(driver, By.XPATH, caminho)

def marcar_checkbox(driver, seletor):
	checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, seletor)))
	if not checkbox.is_selected():
		checkbox.click()

def desmarcar_checkbox(driver, seletor):
	checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, seletor)))
	if checkbox.is_selected():
		checkbox.click()

def selecionar_operacao(driver, valor):
	selectelement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, SELETOR_OPERACAO)))
	Select(selectelement).select_by_value(str(valor))

def preencher_periodo(driver, data_ini, data_fim):
	campo_ini = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, SELETOR_DATA_INICIAL)))
	campo_fim = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, SELETOR_DATA_FINAL)))
	campo_ini.clear()
	campo_ini.send_keys(data_ini)
	campo_fim.clear()
	campo_fim.send_keys(data_fim)

def clicar_consultar(driver):
	botao = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, SELETOR_BOTAO_CONSULTAR)))
	botao.click()
	try:
		WebDriverWait(driver, 3).until(EC.alert_is_present())
		alerta = driver.switch_to.alert
		alerta.accept()
	except:
		pass