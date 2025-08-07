from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select

from selenium.webdriver.support import expected_conditions as EC

from seletores import *

def esperareclicar(driver, by, seletor, timeout=10):

elemento = WebDriverWait(driver, timeout).until(EC.elementtobe_clickable((by, seletor)))

elemento.click()

return elemento

def clicar_aba(driver, nome):

caminho = XPATH_ABA.format(nome)

esperareclicar(driver, By.XPATH, caminho)

def marcar_checkbox(driver, seletor):

checkbox = WebDriverWait(driver, 10).until(EC.elementtobeclickable((By.CSSSELECTOR, seletor)))

if not checkbox.is_selected():

checkbox.click()

def desmarcar_checkbox(driver, seletor):

checkbox = WebDriverWait(driver, 10).until(EC.elementtobeclickable((By.CSSSELECTOR, seletor)))

if checkbox.is_selected():

checkbox.click()

def selecionar_operacao(driver, valor):

selectelement = WebDriverWait(driver, 10).until(EC.elementtobeclickable((By.CSSSELECTOR, SELETOROPERACAO)))

Select(selectelement).selectby_value(str(valor))

def preencherperiodo(driver, dataini, data_fim):

campoini = WebDriverWait(driver, 10).until(EC.elementtobeclickable((By.CSSSELECTOR, SELETORDATA_INICIAL)))

campofim = WebDriverWait(driver, 10).until(EC.elementtobeclickable((By.CSSSELECTOR, SELETORDATA_FINAL)))

campo_ini.clear()

campoini.sendkeys(data_ini)

campo_fim.clear()

campofim.sendkeys(data_fim)

def clicar_consultar(driver):

botao = WebDriverWait(driver, 10).until(EC.elementtobeclickable((By.CSSSELECTOR, SELETORBOTAOCONSULTAR)))

botao.click()

try:

WebDriverWait(driver, 3).until(EC.alertispresent())

alerta = driver.switch_to.alert

alerta.accept()

except:

pass