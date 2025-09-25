class Impresion:
    def __init__(self):
        self.items = []

    def enqueue(self, nombreDocumento, tamaño):
        self.items.append((nombreDocumento, tamaño))

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

colaImpresion = Impresion()
numDocumentos = int(input("Ingrese la cantidad de documentos que se van a imprimir : "))

for i in range(numDocumentos):
    nombre = input(f"Ingrese el nombre de la persona que envía el documento #{i + 1}: ")
    tamaño = input(f"Ingrese el tamaño del documento # {i + 1}:  ")
    colaImpresion.enqueue(nombre, tamaño)

print("\n--- Iniciando proceso de impresión ---\n")

while not colaImpresion.is_empty():
    documento = colaImpresion.dequeue()
    print(f"Imprimiendo documento de {documento[0]} - Tamaño: {documento[1]}")

print("\nTodos los documentos han sido impresos.")