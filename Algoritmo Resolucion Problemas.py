""" 
TODO: Ejercicio 15== Calcular la suma de digitos de un número entero.
!Para este ejercicio se puede solicitar el numero en forma de str 
!descomponerlo en una lista con un ciclo for y por cada valor que se vaya
!agregando, transfrormarlo a int y sumarlo ya sea en una variable independiente
!o en una lista y luego sumarlo con la funcion sum() 


Por ejemplo:
numero = str(input("Ingrese un numero: "))
listaDigitos = [int(digito) for digito in numero]
sum(listaDigitos) #!e imprimimos el resultado en otrea linea con agregados
"""
#////////////////////////////////////////////////////////////////////////////////////////////////////////
""" 
TODO: Ejercicio 19 == Comprobar si un numero es primo
*Guardamos en una variable "n" el numero a comprobar
*como los numeros primos son todos aquellos numeros que son divisibles
*entre si mismos y entre 1, entonces podemos hacer un ciclo
*while que vaya obteniendo el modulo del numero "n" 
*dividido entre todos los numeros (incluido si mismo) hasta que llegue al 1
*y creamos una condicion en la que si el modulo es <= que 0 o 1, detenga el proceso
* y si el ciclo termina y no se cumple la condicion, entonces el numero es primo

Por ejemplo:
n = int(input("Ingrese un número: "))
es_primo = True

if n <= 1:
    es_primo = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            es_primo = False
            break

if es_primo:
    print("El número es primo")
else:
    print("El número no es primo")


"""
#//////////////////////////////////////////////////////////////////////////////////////////////
""" 
TODO: Ejercicio 20 == Calcular todas las combinaciones posibles de una cadena
!Con este algoritmo, podemos calcular las combinaciones posibles de una cadena
!usando recursividad y concatenacion de cadenas, elegimos una letra y la separamos
!del resto de la cadena, y luego llamamos a la funcion recursivamente con el resto
!de la cadena, y por cada combinacion que se genere, le agregamos la letra que
!separamos al inicio, y asi hasta que la cadena tenga un solo caracter
Por ejemplo:
def generar_combinaciones(cadena):
    if len(cadena) <= 1:
        return [cadena]
    
    combinaciones = []
    
    for i in range(len(cadena)):
        letra = cadena[i]
        resto = cadena[:i] + cadena[i+1:]
        
        for subcombinacion in generar_combinaciones(resto):
            combinaciones.append(letra + subcombinacion)
    
    return combinaciones

entrada = "abc"
resultado = generar_combinaciones(entrada)
print(resultado)
"""