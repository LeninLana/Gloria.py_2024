#Elaborar uma rotina que simule o valor das parcelas de um empréstimo que usa juros compostos. Adotar taxa de juros 5% ao mês
#M = montante
#C = capital
#Tx = taxa
#Tp = tempo
#D = desistencia

def juros():
    while True:
        C = float(input('Qual é o valor? '))
        Tp = int(input('Quantas vezes? '))

        Tx = 0.05 * Tp
        parenteses = Tx + 1
        conta_2 = C * parenteses
        conta_1 = conta_2 ** Tp
        M = conta_1
        Mm = M / Tp

        print(f'Você deverá o total de {M:.2f} com prestações de {Mm:.2f} mensais')

        D = input('Deseja continuar? (s/n) ')
        if D != 's':
            break
juros()


