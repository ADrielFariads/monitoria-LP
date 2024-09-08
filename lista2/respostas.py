import math

def exercicio1(vetor: tuple) -> int:
    if not isinstance(vetor, tuple|list):
         raise TypeError("O Argumento recebido incorreto. O Argumento deve ser uma lista ou uma tupla!")


    resultado = 0
    for cada_elemento in vetor:
        if not isinstance(cada_elemento, int|float):
            raise TypeError("Uma das entradas não é um número!")

        resultado += cada_elemento**2

    return math.sqrt(resultado)    



def exercicio2(ponto_1: tuple, ponto_2: tuple) -> tuple:

    if not (isinstance(ponto_1, tuple) and isinstance(ponto_2, tuple)):
        raise TypeError("Os argumentos inseridos devem ser tuplas!")
    if ponto_1 == ponto_2:
        raise ValueError("Os pontos inseridos são iguais! Não existe uma única reta definida por eles.")
    if ponto_1[0] == ponto_2[0]:
        raise ValueError("Os pontos inseridos formam uma reta vertical.")
    
    a = (ponto_1[1]-ponto_2[1])/(ponto_1[0]-ponto_2[0]) #coeficiente angular
    b = ponto_1[1]-ponto_1[0]*a

    return (a, b)


