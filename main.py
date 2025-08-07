from navegador import criardriver, fechardriver
from seletores import SELETOR_CNPJ

from acoes import clicaraba, selecionaroperacao, preencher_periodo

from capturas import fazer_captura

def main():

driver = criar_driver()

driver.get("AURLDOSEUSISTEMA")

# Seleciona os CNPJs

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

cnpj_links = WebDriverWait(driver, 10).until(

EC.presenceofallelementslocated((By.CSSSELECTOR, SELETORCNPJ))

)

for i in range(len(cnpj_links)):

try:

cnpj_links[i].click()

clicar_aba(driver, "Extratos")

clicar_aba(driver, "NF-e / NFC-e")

# Chame aqui as funções do fluxo, operações etc

selecionar_operacao(driver, 1)

preencher_periodo(driver, "01/01/2024", "31/01/2024")

fazercaptura(driver, f"empresa{i+1}_op1.png")

# ... continue o fluxo conforme especificado

driver.back()

cnpjlinks = driver.findelements(By.CSSSELECTOR, SELETORCNPJ)

except Exception as e:

print(f"Erro na empresa {i+1}: {e}")

fechar_driver(driver)

if name == "main":

main()