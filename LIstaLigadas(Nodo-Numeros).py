"""    
?Aguileta Argueta Mario Damián 
*Ejercicios Unidad 3: Estructura de Datos
?Fecha: 21/06/2025
"""

class NodoNumeros:
    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None

class ListaLigadaNumeros:
    def __init__(self):
        self.cabeza = None

    def agregar(self, numero):
        nuevo_nodo = NodoNumeros(numero)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        if not self.cabeza:
            print("La lista está vacía.")
            return
        actual = self.cabeza
        while actual:
            print(actual.numero, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
lista = ListaLigadaNumeros()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)
lista.mostrar()