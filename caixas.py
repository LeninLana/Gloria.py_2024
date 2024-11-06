#fila = [3,5,8,1,2,5,5,3,4,6]
#3 caixas
#fila única
#quantidade de atendimento por caixa
#tempo médio de atendimento de cada caixa
#tempo = tempo + 1
#Fazer um código que reconheça a fila única, pedir a quantidade de pessoas na fila, quanto tempo cada cliente passou em cada caixa, calcular a média de tempo de atendimento de cada caixa com base nessas informações e imprimir essa média de tempo de atendimento de cada caixa
#QPF = QUANTIDADE DE PESSOAS NA FILA
#QPC+N = QUANTIDADE DE PESSOAS NO CAIXA TAL
#T+N = TEMPO DE ATENDIMENTO DE CAIXA TAL

qpf = int(input('Quantas pessoas passaram na fila? '))
qpc1 = int(input('Quantas pessoas passaram pelo caixa 1? '))
qpc2 = int(input('Quantas pessoas passaram pelo caixa 2? '))
qpc3 = int(input('Quantas pessoas passaram pelo caixa 3? '))
t1 = int(input('Qual tempo total de atendimento do caixa 1 em minutos? '))
t2 = int(input('Qual tempo total de atendimento do caixa 2 em minutos? '))
t3 = int(input('Qual tempo total de atendimento do caixa 3 em minutos? '))

calc1 = t1 / qpc1
calc2 = t2 / qpc2
calc3 = t3 / qpc3

recusar = qpc1 + qpc2 + qpc3

if recusar > qpf:
    print('A soma de pessoas para cada fila não pode ser maior do que a quantidade total de pessoas na fila.')

elif recusar < qpf:
    print('A soma pessoas para cada fila não pode ser menor do que a quantidade total de pessoas na fila.')

else:
    print(f'A média do tempo de atendimento do caixa 1 foi de {calc1} minutos por pessoa, a do caixa 2 foi {calc2} e a do caixa 3 foi de {calc3}')

