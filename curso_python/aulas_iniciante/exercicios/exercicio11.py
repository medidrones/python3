"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Jorge
"""
lista = ['Maria', 'Helena', 'Jorge']
lista.append('João')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))