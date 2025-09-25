#Ejercicio que ejemplifica la recursividad con el problema de la torre de hanoi
#Este es solo un ejercicio muestra de una posible solucion usado como analisis
def torre_hanoi(n, origen, destino_resuelto, auxiliar):
    if n == 1: 
        print("Disco origen", origen, "rojo (origen)", destino_resuelto)
    else:
        torre_hanoi(n-1, origen, auxiliar, destino_resuelto)
        print("disco de salida", origen, "Azul (a resuelto)", destino_resuelto)
        torre_hanoi(n-1, auxiliar, destino_resuelto, origen)

# numeros de parametros 
n = 3
torre_hanoi(n, "Rojo", "Verde", "Azul")
