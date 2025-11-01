"""    
?Aguileta Argueta Mario Damián 
*Ejercicios Unidad 3: Estructura de Datos
?Fecha: 21/06/2025
"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaLigada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def remover_duplicados(self):
        if not self.cabeza:
            return

        vistos = set()
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.dato in vistos:
                anterior.siguiente = actual.siguiente
            else:
                vistos.add(actual.dato)
                anterior = actual
            actual = actual.siguiente

    def mostrar(self):
        if not self.cabeza:
            print("La lista está vacía.")
            return
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
lista = ListaLigada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(2)
lista.agregar(3)
lista.agregar(1)
lista.mostrar()

lista.remover_duplicados()
lista.mostrar()