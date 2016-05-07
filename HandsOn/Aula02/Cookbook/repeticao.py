#!/usr/bin/python
import sys

# dicionarios
servidor = {'nome':'DNS',
            'vcpus': 4,
            'memoria': 2048,
            'disco': [{'vda':'50G'},{'vdb':'50G'}]
            }

for letra in 'python':
    if letra == 'h':
        print 'letra H encontrada'



# matrizes
matriz = [[1, 2, 3, 4],
          [5, 6, 7, 8]]

print matriz[0][2]

lista = ['python', 'c', 'asp', 'vb', 'ruby', 'nodejs', 'java', 'go']
for item in lista:
    if item == 'nodejs':
        print 'nodejs encontrado'
        break
else:
     print 'Nao existe nodejs na lista'


valor = ''
print 'Digite #sair para sair.'
while (valor != '#sair'):
    valor = raw_input('Digite uma opcao: ')


'''
contador = 1

while (contador < 10):
    print contador
    contador += 1

for i in range(0,10):
    print i
'''