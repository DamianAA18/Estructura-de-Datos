"""    
?Aguileta Argueta Mario Damián 
*Ejercicios Unidad 3: Estructura de Datos
?Fecha: 21/06/2025
"""
class NodoCiclosClase:
    def __init__(self, ciclo):
        self.ciclo = ciclo  
        self.siguiente = None

class ListaCiclosClase:
    def __init__(self):
        self.cabeza = None

    def agregar(self, ciclo):
        nuevo_nodo = NodoCiclosClase(ciclo)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        if not self.cabeza:
            print("No hay ciclos registrados.")
            return
        actual = self.cabeza
        while actual:
            print(f"Ciclo: {actual.ciclo}", end=" -> ")
            actual = actual.siguiente
        print("Fin")

# Ejemplo de uso
lista = ListaCiclosClase()
lista.agregar("Primavera 2023")
lista.agregar("Otoño 2023")
lista.agregar("Primavera 2024")
lista.mostrar()