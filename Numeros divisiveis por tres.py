
#Mostrar todos os números naturais divisíveis por 3 existentes em um intervalo qualquer

n1 = int(input("Digite o início do intervalo: "))
n2 = int(input("Digite o fim do intervalo: "))

if n1 > n2:
    print("Certifique-se de que o início seja menor ou igual ao fim.")
else:
    print(f"Números inteiros divisíveis por 3 no intervalo de {n1} a {n2}:")
    
    for num in range(n1, n2 + 1):
        if num % 3 == 0:
            elif 
            print(num)
