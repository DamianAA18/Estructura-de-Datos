"""    
?Aguileta Argueta Mario Damián 
*Ejercicios Unidad 3: Estructura de Datos
?Fecha: 21/06/2025
"""
class Nodo: 
    def _init_(self, dato): 
        self.dato = dato 
        self.siguiente = None   # Apunta al siguiente nodo 
        self.anterior=None # Apunta al nodo anterior
class ListaCircular: 
    def _init_(self): 
        self.cabeza = None 
        self.cola=None 
    def agregar(self, dato): 
        nuevo_nodo= Nodo(dato) 
        if not self.cabeza: 
            self.cabeza = nuevo_nodo 
            self.cabeza.siguiente = nuevo_nodo  # Apunta a sí mismo 
        else: 
            actual = self.cabeza 
            while actual.siguiente != self.cabeza: 
                actual = actual.siguiente 
            actual.siguiente = nuevo_nodo 
            nuevo_nodo.siguiente = self.cabeza  
    def mostrar(self): 
        if not self.cabeza: 
            print("La lista está vacía.") 
            return 
        actual = self.cabeza 
        while True: 
            print(actual.dato, end=" -> ") 
            actual = actual.siguiente 
            if actual == self.cabeza: 
                break 
        print("(circular)") 

    def eliminar(self, dato):
        if not self.cabeza:
            return
        
        actual = self.cabeza
        previo = None
        
        while True:
            if actual.dato == dato:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    # Si es el único nodo
                    if actual.siguiente == self.cabeza:
                        self.cabeza = None
                    else:
                        actual.dato=actual.siguiente.dato
                        actual.siguiente=actual.siguiente.siguiente
                return
            previo = actual

    def buscar(self, dato):
        if not self.cabeza:
            return -1
        actual=self.cabeza
        poscion=0
        while True:
            if actual.dato==dato:
                return poscion
            actual=actual.siguiente
            poscion+=1
            if actual==self.cabeza:
                break
        
        while True:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return False


lista=ListaCircular()
while True:
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Eliminar")
    print("4. Buscar")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        dato = input("Ingrese el dato a agregar: ")
        lista.agregar(dato)
    elif opcion == "2":
        lista.mostrar()
    elif opcion == "3":
        dato = input("Ingrese el dato a eliminar: ")
        lista.eliminar(dato)
    elif opcion == "4":
        dato = input("Ingrese el dato a buscar: ")
        posicion = lista.buscar(dato)
        if posicion != -1:
            print(f"El dato {dato} fue encontrado en la posición {posicion}.")
        else:
            print(f"El dato {dato} no fue encontrado en la lista.")
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Intente de nuevo.")