from collections import deque

# Definición de un grafo como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(grafo, inicio):
    visitados = set()  # Conjunto para llevar un registro de los nodos visitados
    cola = deque()     # Cola para mantener los nodos que se deben explorar

    cola.append(inicio)
    visitados.add(inicio)

    while cola:
        nodo = cola.popleft()
        print(nodo, end=' ')

        for vecino in grafo[nodo]:
            if vecino not in visitados:
                cola.append(vecino)
                visitados.add(vecino)

# Llamamos a la función BFS comenzando desde el nodo 'A'
print("Recorrido BFS desde el nodo 'A':")
bfs(grafo, 'A')
