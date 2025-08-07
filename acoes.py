from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from seletores import *

def esperar_click(driver, by, seletor, timeout=10):

return WebDriverWait(driver, timeout).until(EC.elementtobe_clickable((by, seletor)))

def clicaraba(driver, textoaba):

aba = WebDriverWait(driver, 10).until(

EC.elementtobeclickable((By.XPATH, f"//a[contains(text(), '{textoaba}')]")))

aba.click()

def selecionar_operacao(driver, valor):

select = esperarclick(driver, By.CSSSELECTOR, SELETOR_OPERACAO)

from selenium.webdriver.support.ui import Select

Select(select).selectbyvalue(str(valor))

def preencherperiodo(driver, datainicial, data_final):

campoini = esperarclick(driver, By.CSSSELECTOR, SELETORDATA_INICIAL)

campofim = esperarclick(driver, By.CSSSELECTOR, SELETORDATA_FINAL)

campoini.clear(); campoini.sendkeys(datainicial)

campofim.clear(); campofim.sendkeys(datafinal)