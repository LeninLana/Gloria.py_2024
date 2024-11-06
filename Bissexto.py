def bissexto():
    ano = int(input('Digite o ano que deseja saber se é bissexto: '))
    if (ano % 4 == 0 and ano % 100 != 0):
    
        print(f'O ano {ano} é bissexto')

    else:
        False
        print(f'O ano {ano} não é bissexto')
        
    
bissexto()