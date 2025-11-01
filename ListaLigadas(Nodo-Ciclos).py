"""    
?Aguileta Argueta Mario Damián 
*Ejercicios Unidad 3: Estructura de Datos
?Fecha: 21/06/2025
"""

class NodoCiclos:
    def __init__(self, nombre_ciclo):
        self.nombre_ciclo = nombre_ciclo
        self.siguiente = None

class ListaLigadaCiclos:
    def __init__(self):
        self.cabeza = None

    def agregar(self, nombre_ciclo):
        nuevo_nodo = NodoCiclos(nombre_ciclo)
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
            print(f"Ciclo: {actual.nombre_ciclo}", end=" -> ")
            actual = actual.siguiente
        print("Fin")

# Ejemplo de uso
lista = ListaLigadaCiclos()
lista.agregar("Planeación")
lista.agregar("Ejecución")
lista.agregar("Evaluación")
lista.mostrar()