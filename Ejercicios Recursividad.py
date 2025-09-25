class Recursivos:
    # 1. Factorial
    def factorial(self, n):
        if n == 1:
            return 1
        else:
            return n * self.factorial(n-1)

    # 2. Suma de naturales
    def suma_natural(self, n):
        if n == 1:
            return 1
        else:
            return n + self.suma_natural(n-1)

    # 3. Contar dígitos
    def contar_digitos(self, n):
        if n < 10:
            return 1
        else:
            return 1 + self.contar_digitos(n // 10)

    # 4. Potencia
    def potencia(self, a, b):
        if b == 0:
            return 1
        else:
            return a * self.potencia(a, b-1)

    # 5. Fibonacci
    def fibonacci(self, n):
        if n == 0 or n == 1:
            return n
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)

    # 6. Contar vocales
    def contar_vocales(self, cadena):
        if cadena == "":
            return 0
        else:
            if cadena[0].lower() in 'aeiou':
                return 1 + self.contar_vocales(cadena[1:])
            else:
                return self.contar_vocales(cadena[1:])

    # 7. Suma lista
    def suma_lista(self, lista):
        if not lista:
            return 0
        else:
            return lista[0] + self.suma_lista(lista[1:])

    # 8. MCD
    def mcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.mcd(b, a % b)

    # 9. Palíndromo
    def es_palindromo(self, palabra):
        if len(palabra) <= 1:
            return True
        elif palabra[0] != palabra[-1]:
            return False
        else:
            return self.es_palindromo(palabra[1:-1])

    # 10. Invertir cadena
    def invertir_cadena(self, cadena):
        if len(cadena) == 0:
            return cadena
        else:
            return cadena[-1] + self.invertir_cadena(cadena[:-1])

    # 11. Buscar elemento en lista
    def buscar_elemento(self, lista, elemento):
        if not lista:
            return False
        elif lista[0] == elemento:
            return True
        else:
            return self.buscar_elemento(lista[1:], elemento)

    # 12. Multiplicación recursiva
    def multiplicar(self, a, b):
        if b == 0:
            return 0
        else:
            return a + self.multiplicar(a, b-1)

    # 13. Decimal a binario
    def decimal_a_binario(self, n):
        if n == 0:
            return ''
        else:
            return self.decimal_a_binario(n // 2) + str(n % 2)

    # 14. Contar carácter
    def contar_caracter(self, cadena, caracter):
        if cadena == "":
            return 0
        else:
            if cadena[0] == caracter:
                return 1 + self.contar_caracter(cadena[1:], caracter)
            else:
                return self.contar_caracter(cadena[1:], caracter)
    #15. Suma de dígitos
    def suma_digitos(self, n):
        if n == 0:
            return 0
        else:
            return n % 10 + self.suma_digitos(n // 10)

    # 16. Pirámide
    def piramide(self, n) :
        if n == 0:
            return
        self.piramide(n-1)
        print('*' * n)

    # 17. Combinaciones
    def combinaciones(self, cadena, actual=""):
        if cadena == "":
            print(actual)
        else:
            self.combinaciones(cadena[1:], actual + cadena[0])
            self.combinaciones(cadena[1:], actual)

    # 18. Torres de Hanoi
    def hanoi(self, n, origen, destino, auxiliar):
        if n == 1:
            print(f"Mover disco de {origen} a {destino}")
        else:
            self.hanoi(n-1, origen, auxiliar, destino)
            self.hanoi(1, origen, destino, auxiliar)
            self.hanoi(n-1, auxiliar, destino, origen)

    # 19. Es primo
    def es_primo(self, n, divisor=2):
        if n <= 2:
            return n == 2
        if n % divisor == 0:
            return False
        if divisor * divisor > n:
            return True
        return self.es_primo(n, divisor+1)

    # 20. Permutaciones
    def permutaciones(self, lista, inicio=0):
        if inicio == len(lista) - 1:
            print(lista)
        else:
            for i in range(inicio, len(lista)):
                lista[inicio], lista[i] = lista[i], lista[inicio]
                self.permutaciones(lista, inicio + 1)
                lista[inicio], lista[i] = lista[i], lista[inicio]

    #21 factorial agregado
    def factorial_agregado(self,n):
        if n < 0:
            return "Error: El número debe ser no negativo."
        elif n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial_agregado(n - 1) 


    #EXTRA #DECIFRRADO ASCII
    def descifrar_ascii(self, codigo):
        if codigo == "":
            return ""
        else:
            partes = codigo.split(" ", 1)
            char = chr(int(partes[0]))
            return char + self.descifrar_ascii(partes[1] if len(partes) > 1 else "") 
        
# MENU
def menu():
    obj = Recursivos()

    while True:
        print("""MENÚ DE EJERCICIOS"
        1. Factorial de un número"
        "2. Suma de números naturales"
        "3. Contar dígitos de un número"
        "4. Calcular potencia"
        "5. Números de Fibonacci"
        "6. Contar vocales en una cadena"
        "7. Sumar elementos de una lista"
        "8. Calcular MCD (máximo común divisor)"
        "9. Verificar si una palabra es palíndromo"
        "10. Invertir una cadena"
        "11. Buscar un elemento en una lista"
        "12. Multiplicación por sumas sucesivas"
        "13. Convertir número decimal a binario"
        "14. Contar ocurrencias de un carácter en una cadena"
        "15. Calcular la suma de dígitos de un número"
        "16. Dibujar pirámide de asteriscos"
        "17. Generar todas las combinaciones de una cadena"
        "18. Resolver las Torres de Hanoi"
        "19. Comprobar si un número es primo"
        "20. Generar todas las permutaciones posibles de una lista"
        "0. Salir""")


        opcion = input("\nElige una opción: ")

        if opcion == "0":
            print("Saliendo...")
            break

        elif opcion == "1":
            n = int(input("Ingresa un número: "))
            print("Resultado:", obj.factorial(n))

        elif opcion == "2":
            n = int(input("Ingresa un número: "))
            print("Resultado:", obj.suma_natural(n)) #uso de la funcion para resolver el problema
            
        elif opcion == "3":
            n = int(input("Ingresa un número: "))
            print("Resultado:", obj.contar_digitos(n))

        elif opcion == "4":
            a = int(input("Base: "))
            b = int(input("Exponente: "))
            print("Resultado:", obj.potencia(a, b))

        elif opcion == "5":
            n = int(input("Posición en Fibonacci: "))
            print("Resultado:", obj.fibonacci(n))

        elif opcion == "6":
            cad = input("Ingresa una cadena: ")
            print("Resultado:", obj.contar_vocales(cad))

        elif opcion == "7":
            lista = list(map(int, input("Ingresa lista de números separados por espacio: ").split()))
            print("Resultado:", obj.suma_lista(lista))

        elif opcion == "8":
            a = int(input("Primer número: "))
            b = int(input("Segundo número: "))
            print("Resultado:", obj.mcd(a, b))

        elif opcion == "9":
            palabra = input("Ingresa una palabra: ")
            print("Resultado:", obj.es_palindromo(palabra))

        elif opcion == "10":
            cad = input("Ingresa una cadena: ")
            print("Resultado:", obj.invertir_cadena(cad))

        elif opcion == "11":
            lista = list(map(int, input("Ingresa lista de números: ").split()))
            elem = int(input("Elemento a buscar: "))
            print("Resultado:", obj.buscar_elemento(lista, elem))

        elif opcion == "12":
            a = int(input("Primer número: "))
            b = int(input("Segundo número: "))
            print("Resultado:", obj.multiplicar(a, b))

        elif opcion == "13":
            n = int(input("Número decimal: "))
            print("Resultado:", obj.decimal_a_binario(n))

        elif opcion == "14":
            cad = input("Cadena: ")
            car = input("Carácter a contar: ")
            print("Resultado:", obj.contar_caracter(cad, car))

        elif opcion == "15":
            n = int(input("Número: "))
            print("Resultado:", obj.suma_digitos(n))

        elif opcion == "16":
            n = int(input("Número de filas: "))
            obj.piramide(n)

        elif opcion == "17":
            cad = input("Cadena: ")
            obj.combinaciones(cad)

        elif opcion == "18":
            n = int(input("Número de discos: "))
            obj.hanoi(n, "A", "C", "B")

        elif opcion == "19":
            n = int(input("Número: "))
            print("Resultado:", obj.es_primo(n))

        elif opcion == "20":
            lista = list(input("Ingresa elementos separados (sin comas): "))
            obj.permutaciones(lista)

        elif opcion == "21":
            n = int(input("Ingresa un número: "))
            print("Resultado:", obj.factorial_agregado(n))

        elif opcion == "22":
            codigo = input("Ingresa el código ASCII separado por espacios: ")
            print("Resultado:", obj.descifrar_ascii(codigo))

        else:
            print("Opción no válida")


# Ejecutar menú
menu()