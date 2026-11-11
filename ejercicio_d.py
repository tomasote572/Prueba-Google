import sys

# EJERCICIO D: Chain Reactions (Code Jam 2022)
# Tema: Árboles y Algoritmo Voraz

def resolver():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    it = iter(entrada)
    t = int(next(it))  # Número de casos
    for caso in range(1, t + 1):
        n = int(next(it))  # Número de módulos
        F = [int(next(it)) for _ in range(n)]  # Diversión de cada módulo
        P = [int(next(it)) for _ in range(n)]  # Puntero de cada módulo
        # Construir listas de hijos para cada nodo (0 es el abismo)
        hijos = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            hijos[P[i - 1]].append(i)
        valor = [0] * (n + 1)
        total = 0
        # Procesar bottom-up desde n hasta 1 (los padres siempre tienen índice menor)
        for i in range(n, 0, -1):
            mis_hijos = hijos[i]
            if not mis_hijos:
                # Nodo hoja (iniciador)
                valor[i] = F[i - 1]
            else:
                menor = float('inf')
                suma = 0
                for h in mis_hijos:
                    val = valor[h]
                    suma += val
                    if val < menor:
                        menor = val
                # Todos los caminos excepto el menor se cierran y se suman al total
                total += (suma - menor)
                # El camino menor continúa y se actualiza con max(F[i], menor)
                valor[i] = max(F[i - 1], menor)
        # Sumar los caminos que llegaron al abismo (hijos del nodo 0)
        for h in hijos[0]:
            total += valor[h]
        print(f"Case #{caso}: {total}")
if __name__ == "__main__":
    resolver()

