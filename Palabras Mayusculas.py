"""
?Crea una función que reciba un string de cualquier tipo y se encargue de 
?poner en mayuscula la primer letra de cada palabra    
"""
"""
!Usamos un algoritmo no deterministico
"""

texto=input("Ingrese el texto a convertir: ")
lista=texto.split()
for i in lista:
    resultado=" ".join([i[0].upper()+i[1:] for i in lista])
print(resultado)

