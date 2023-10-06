def entrada():
    numeros = []
    i = 0
    while i < 2:
        numeros.append(float(input(f"Digite o número {i + 1}: ")))
        i += 1 # Isto é o mesmo que escrever i = i + 1
    return numeros


def saida(numero_1: float, numero_2: float, subtracao: float) -> None:
    print(f"O resultado da subtração do número {numero_1} do número {numero_2} é igual a {subtracao}.")
    
