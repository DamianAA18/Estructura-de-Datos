#Ejercicio que toma una ecuacion matematica y verifica si los parentesis
#estan correctamente balanceados usando una pila y recursividad
class ParentesisCorrectos():
    def __init__(self, cadenaC):
        self.cadendaC = cadenaC

    def proceso(self):
        pila = []
        for i in self.cadendaC:
            if i == '(':
                pila.append(i)
            elif i == ')':
                if not pila:
                    return False
                pila.pop()
        return len(pila) == 0
obj=ParentesisCorrectos(input("Ingrese una formula matematica: "))
print(obj.proceso())