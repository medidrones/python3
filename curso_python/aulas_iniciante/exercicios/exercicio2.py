nome = 'Jorge Medina'
altura = 1.76
peso = 75
imc = peso / (altura * altura) # Primeira forma de realizar o cálculo.
imc2 = peso / altura ** 2 # Segunda forma de realizar o cálculo.
print(imc)
print(imc2)

# Exibição com strings
print(nome, 'tem', altura, 'de altura, pesa', peso, 'quilos e seu IMC é', imc)

# Exibição com Concatenação
print(nome + ' ' + 'tem' + ' ' + str(float(altura)) + ' ' + 'de altura, pesa' + ' ' + str(int(peso)) + ' ' + 'quilos e seu IMC é' + ' ' + str(float(imc)))