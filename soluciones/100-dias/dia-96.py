"""
        Bienvenido al día 96 de #100diasdepython        
                    El reto de hoy es:
Crea una funcion que use argumentos arbitrarios de tipo 
Keyword para recibir nombre, apellido y edad y devuelva 
estos argumetos en un diccionario en el siguiente formato 
    {"nombre": "Pepito", "apellido":"Perez","edad":25} 
                Imprime el resultado
"""


def persona(**atributos):
    resultado = dict()
    for key, value in atributos.items():
        resultado[key] = value
    return resultado


print(persona(nombre="Pepito", apellido="Perez", edad=25))
# Resutado: {'nombre': 'Pepito', 'apellido': 'Perez', 'edad': 25}
