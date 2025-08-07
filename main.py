from navegador import criardriver, fechardriver
from seletores import SELETORCNPJ, SELETORNFE, SELETORNFCE, SELETORTOTALIZADO

from acoes import clicaraba, marcarcheckbox, desmarcarcheckbox, selecionaroperacao, preencherperiodo, clicarconsultar

from capturas import fazer_captura

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.sefaz.rs.gov.br/Receita/PainelUsuario.aspx"

DATA_INICIAL = "01/01/2024"

DATA_FINAL = "31/01/2024"

def fluxoempresa(driver, nomearquivo_prefixo):

# Abre aba "Extratos" > "NF-e / NFC-e"

clicar_aba(driver, "Extratos")

clicar_aba(driver, "NF-e / NFC-e")

# Captura 1

marcarcheckbox(driver, SELETORNFE)

marcarcheckbox(driver, SELETORNFCE)

selecionar_operacao(driver, 1)

preencherperiodo(driver, DATAINICIAL, DATA_FINAL)

clicar_consultar(driver)

fazercaptura(driver, f"{nomearquivoprefixo}nfenfceop1.png")

# Captura 2

selecionar_operacao(driver, 5)

clicar_consultar(driver)

fazercaptura(driver, f"{nomearquivoprefixo}nfenfceop5.png")

# Captura 3

marcarcheckbox(driver, SELETORNFE)

desmarcarcheckbox(driver, SELETORNFCE)

selecionar_operacao(driver, 2)

clicar_consultar(driver)

fazercaptura(driver, f"{nomearquivoprefixo}nfe_op2.png")

# Captura 4

selecionar_operacao(driver, 3)

clicar_consultar(driver)

fazercaptura(driver, f"{nomearquivoprefixo}nfe_op3.png")

# Aba "CT-e"

clicar_aba(driver, "CT-e")

marcarcheckbox(driver, SELETORTOTALIZADO)

preencherperiodo(driver, DATAINICIAL, DATA_FINAL)

clicar_consultar(driver)

fazercaptura(driver, f"{nomearquivoprefixo}cte.png")

def main():

driver = criar_driver()

driver.get(URL)

cnpj_links = WebDriverWait(driver, 10).until(

EC.presenceofallelementslocated((By.CSSSELECTOR, SELETORCNPJ)))

for i in range(len(cnpj_links)):

try:

cnpj_links[i].click()

fluxoempresa(driver, f"empresa{i+1}")

driver.back()

cnpjlinks = driver.findelements(By.CSSSELECTOR, SELETORCNPJ)

except Exception as e:

print(f"Erro na empresa {i+1}: {e}")

fechar_driver(driver)

if name == "main":

main()