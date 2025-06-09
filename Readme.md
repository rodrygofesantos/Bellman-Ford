 Algoritmo de Bellman-Ford – Aplicação Didática

Este projeto apresenta a aplicação do **algoritmo de Bellman-Ford** sobre um grafo direcionado e ponderado, com foco em aprendizado e visualização de caminhos mínimos a partir de um único vértice.

## Objetivo

Determinar o **caminho mínimo a partir do vértice `r`** para todos os demais vértices de um grafo direcionado com pesos positivos.

---

## Estrutura do Grafo

O grafo contém os seguintes vértices e arestas (com pesos):

```
r → s  peso 3  
r → u  peso 5  
r → t  peso 7  
s → u  peso 1  
s → t  peso 3  
u → t  peso 1
```

---

## Etapas do Algoritmo

### Inicialização

Cada vértice recebe uma distância inicial de infinito, exceto o vértice de origem `r`, que recebe 0:

| Vértice | Distância Inicial |
|---------|-------------------|
| r       | 0                 |
| s       | ∞                 |
| u       | ∞                 |
| t       | ∞                 |

---

### Iteração 1

Atualizações realizadas ao percorrer todas as arestas:

- r → s: 0 + 3 = 3 → atualiza s
- r → u: 0 + 5 = 5 → atualiza u
- r → t: 0 + 7 = 7 → atualiza t
- s → u: 3 + 1 = 4 → atualiza u (melhora de 5 para 4)
- s → t: 3 + 3 = 6 → atualiza t (melhora de 7 para 6)
- u → t: 4 + 1 = 5 → atualiza t (melhora de 6 para 5)

| Vértice | Distância após Iteração 1 |
|---------|----------------------------|
| r       | 0                          |
| s       | 3                          |
| u       | 4                          |
| t       | 5                          |

---

### Iterações 2 e 3

Nenhuma atualização adicional é feita. O algoritmo termina antecipadamente.

---

## Resultado Final

| Vértice | Menor distância desde `r` |
|---------|----------------------------|
| r       | 0                          |
| s       | 3                          |
| u       | 4                          |
| t       | 5                          |

---

## Caminhos Mínimos

- r → s = 3  
- r → s → u = 3 + 1 = 4  
- r → s → u → t = 3 + 1 + 1 = 5

---

## Observações

- O algoritmo executa em no máximo |V| − 1 iterações (3 neste exemplo).
- É robusto para grafos com arestas negativas (não presentes neste grafo).
- Detecta ciclos negativos (também inexistentes neste caso).

---

## Execução do Código

Para rodar o código com este grafo, utilize o script `bellman_ford.py` disponível neste repositório.
