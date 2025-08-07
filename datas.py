import datetime
import calendar

def periodomesanterior():

	hoje = datetime.date.today()

	primeirodiames_atual = hoje.replace(day=1)

	ultimodiames_anterior = primeirodiames_atual - datetime.timedelta(days=1)

	primeirodiames_anterior = ultimodiames_anterior.replace(day=1)

	return (

		primeirodiames_anterior.strftime("%d/%m/%Y"),

		ultimodiames_anterior.strftime("%d/%m/%Y")

	)

DATAINICIAL, DATAFINAL = periodomesanterior()

print(f"Data inicial: {DATAINICIAL}, Data final: {DATAFINAL}")