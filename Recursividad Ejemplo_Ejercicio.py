def insertarAbajo(pila, elemento):
    if not pila:   # si la pila está vacía
        pila.append(elemento)
    else:
        temp = pila.pop()
        insertarAbajo(pila, elemento)
        pila.append(temp)

def invertirPila(pila):
    if pila:
        temp = pila.pop()
        invertirPila(pila)
        insertarAbajo(pila, temp)

pila = ["Bruno", "Ana", "Luis", "María"]
invertirPila(pila)
print(pila) 