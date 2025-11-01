"""    
?Aguileta Argueta Mario Damián 
*Ejercicios Unidad 3: Estructura de Datos
?Fecha: 21/06/2025
"""
class NodoRecursivo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

    def mostrar(self, inicio):
        print(self.dato, end=" -> ")
        if self.siguiente != inicio:
            self.siguiente.mostrar(inicio)
        else:
            print("(circular)")

class ListaCircularRecursiva:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = NodoRecursivo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cabeza.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza

    def mostrar(self):
        if not self.cabeza:
            print("La lista está vacía.")
        else:
            self.cabeza.mostrar(self.cabeza)

# Ejemplo de uso
lista = ListaCircularRecursiva()
lista.agregar("A")
lista.agregar("B")
lista.agregar("C")
lista.mostrar()