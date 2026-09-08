# Programa para calculo de consumo eletrico. 
# Autor: Carlos Marcelo Silva

# Entrada

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potencia do aparelho em (W): "))
tempo = float(input("Digite o consumo medio diario em horas: "))

# Processamento
# Calculo do consumo mensal em kWh
# Calculo do custo mensal em reais considerando o valor do kWh

consumo_mensal = (potencia * tempo * 30) / 1000
kwh = 0.75
custo_mensal = consumo_mensal * kwh

# Saida

print(f"O consumo mensal do {aparelho} é de {consumo_mensal:.2f} kWh.")
print(f"O custo mensal é de R${custo_mensal:.2f}.")
