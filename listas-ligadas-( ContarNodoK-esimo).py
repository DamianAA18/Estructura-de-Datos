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

    def contar_nodo_k_esimo(self, k):
        actual = self.cabeza
        contador = 1
        while actual:
            if contador == k:
                print(f"El nodo K-ésimo ({k}) contiene: {actual.dato}")
                return
            actual = actual.siguiente
            contador += 1
        print(f"No existe el nodo K-ésimo ({k}) en la lista.")

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
lista.agregar("A")
lista.agregar("B")
lista.agregar("C")
lista.agregar("D")
lista.mostrar()

lista.contar_nodo_k_esimo(3)  
lista.contar_nodo_k_esimo(5)  