"""
        Bienvenido al día 53 de #100diasdepython    
                El reto de hoy es:
    Crea una funcion que reciba una lista de 
numeros y devuelva una lista de los numeros al cuadrado
    Ejecuta la funcion para la lista [2, 3, 5, 7, 11]
                Imprime el resultado
"""


def cuadrados(numeros: list):
    """
    Funcion que eleva al cuadrado cada numero de la lista
    Args:
        numeros (list): lista de numeros
    Returns:
        list: lista de numeros
    """
    cuadrados = [n**2 for n in numeros]
    return cuadrados


lista = [2, 3, 5, 7, 11]
print(cuadrados(lista))
# Resultado: [4, 9, 25, 49, 121]
