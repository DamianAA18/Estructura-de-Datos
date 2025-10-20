import heapq

def dijkstra(grafo, inicio):
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[inicio] = 0

    predecesores = {nodo: None for nodo in grafo}

    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        if distancia_actual > distancias[nodo_actual]:
            continue
        for vecino, peso in grafo[nodo_actual].items():
            distancia_calculada = distancia_actual + peso
            if distancia_calculada < distancias[vecino]:
                distancias[vecino] = distancia_calculada
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia_calculada, vecino))

    return distancias, predecesores

def reconstruir_camino(predecesores, inicio, fin):

    camino = []
    nodo_actual = fin
    while nodo_actual is not None:
        camino.insert(0, nodo_actual)
        nodo_actual = predecesores[nodo_actual]
    if camino[0] == inicio:
        return camino
    else:
        return None 
grafo_ejemplo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}


nodo_inicial = 'A'


distancias, predecesores = dijkstra(grafo_ejemplo, nodo_inicial)


print(f"Resultados del algoritmo de Dijkstra desde el nodo '{nodo_inicial}':")
print("-" * 50)

for nodo, distancia in distancias.items():
    print(f"La distancia más corta a '{nodo}' es: {distancia}")

print("-" * 50)
print("Caminos más cortos:")

for nodo_destino in grafo_ejemplo:
    if nodo_destino != nodo_inicial:
        camino = reconstruir_camino(predecesores, nodo_inicial, nodo_destino)
        if camino:
            print(f"  Camino a '{nodo_destino}': {' -> '.join(camino)}")
        else:
            print(f"  No hay camino desde '{nodo_inicial}' a '{nodo_destino}'")