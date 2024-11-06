C = float(input('Qual é o valor? '))
Tp = int(input('Quantas vezes? '))


Tx = 0.05 * Tp
parenteses = Tx + 1
conta_2 = C * parenteses
conta_1 = conta_2 ** Tp


M = conta_2

print(M)