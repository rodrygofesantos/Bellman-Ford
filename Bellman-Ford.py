# Lista de arestas (origem, destino, peso)
arestas = [
    ("r", "s", 3),
    ("r", "u", 5),
    ("s", "t", 3),
    ("s", "u", 1),
    ("u", "t", 1),
    ("r", "t", 7)
]

# Lista de vértices
vertices = ["r", "s", "t", "u"]


def bellman_ford_trace(origem):
    # Inicialização: todas as distâncias como infinito, exceto a origem
    dist = {v: float("inf") for v in vertices}
    dist[origem] = 0

    print(f"Inicialização:")
    print(dist)
    print("\n")

    # Iterações (|V| - 1 vezes)
    for i in range(len(vertices) - 1):
        print(f"--- Iteração {i + 1} ---")
        atualizado = False

        for u, v, peso in arestas:
            if dist[u] != float("inf") and dist[u] + peso < dist[v]:
                antigo = dist[v]
                dist[v] = dist[u] + peso
                print(f"Aresta ({u} → {v}, peso={peso}): {v} atualizado de {antigo} para {dist[v]}")
                atualizado = True
            else:
                print(f"Aresta ({u} → {v}, peso={peso}): nenhuma atualização")

        print(f"Distâncias após iteração {i + 1}: {dist}\n")

        if not atualizado:
            print("Nenhuma atualização realizada nesta iteração. Encerrando precocemente.\n")
            break

    # Verificação de ciclos negativos
    for u, v, peso in arestas:
        if dist[u] != float("inf") and dist[u] + peso < dist[v]:
            raise ValueError("Ciclo negativo detectado!")

    # Resultado final
    print("--- Resultado Final ---")
    for v in vertices:
        print(f"Distância mínima de {origem} até {v}: {dist[v]}")

    return dist


# Executar a função a partir do vértice 'r'
bellman_ford_trace("r")
