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

    def eliminar_primera_ocurrencia(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.dato == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                print(f"Se eliminó la primera ocurrencia del valor: {valor}")
                return
            anterior = actual
            actual = actual.siguiente

        print(f"El valor {valor} no se encontró en la lista.")

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
lista.agregar(5)
lista.agregar(3)
lista.agregar(7)
lista.agregar(3)
lista.mostrar()

lista.eliminar_primera_ocurrencia(3)
lista.mostrar()