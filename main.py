from navegador import criardriver, fechardriver
from seletores import SELETORCNPJ, SELETORNFE, SELETORNFCE, SELETORTOTALIZADO

from acoes import clicaraba, marcarcheckbox, desmarcarcheckbox, selecionaroperacao, preencherperiodo, clicarconsultar

from capturas import fazer_captura

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.sefaz.rs.gov.br/Receita/PainelUsuario.aspx"

def fluxoempresa(driver, nomearquivo_prefixo):
	# Abre aba "Extratos" > "NF-e / NFC-e"
	clicaraba(driver, "Extratos")
	clicaraba(driver, "NF-e / NFC-e")

	# Captura 1
	marcarcheckbox(driver, SELETORNFE)
	marcarcheckbox(driver, SELETORNFCE)
	selecionaroperacao(driver, 1)
	preencherperiodo(driver, DATAINICIAL, DATA_FINAL)
	clicarconsultar(driver)
	fazer_captura(driver, f"{nomearquivo_prefixo}nfenfceop1.png")

	# Captura 2
	selecionaroperacao(driver, 5)
	clicarconsultar(driver)
	fazer_captura(driver, f"{nomearquivo_prefixo}nfenfceop5.png")

	# Captura 3
	marcarcheckbox(driver, SELETORNFE)
	desmarcarcheckbox(driver, SELETORNFCE)
	selecionaroperacao(driver, 2)
	clicarconsultar(driver)
	fazer_captura(driver, f"{nomearquivo_prefixo}nfe_op2.png")

	# Captura 4
	selecionaroperacao(driver, 3)
	clicarconsultar(driver)
	fazer_captura(driver, f"{nomearquivo_prefixo}nfe_op3.png")

	# Aba "CT-e"
	clicaraba(driver, "CT-e")
	marcarcheckbox(driver, SELETORTOTALIZADO)
	preencherperiodo(driver, DATAINICIAL, DATA_FINAL)
	clicarconsultar(driver)
	fazer_captura(driver, f"{nomearquivo_prefixo}cte.png")


def main():
	driver = criardriver()
	driver.get(URL)
	cnpj_links = WebDriverWait(driver, 10).until(
		EC.presence_of_all_elements_located((By.CSS_SELECTOR, SELETORCNPJ))
	)

	for i in range(len(cnpj_links)):
		try:
			cnpj_links[i].click()
			fluxoempresa(driver, f"empresa{i+1}")
			driver.back()
			cnpj_links = driver.find_elements(By.CSS_SELECTOR, SELETORCNPJ)
		except Exception as e:
			print(f"Erro na empresa {i+1}: {e}")

	fechardriver(driver)


if __name__ == "__main__":
	main()