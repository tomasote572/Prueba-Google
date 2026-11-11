import sys
from collections import defaultdict
import heapq

# EJERCICIO E: Bathroom Stalls (Code Jam 2017)
# Tema: Eficiencia con números grandes / Conteo de Intervalos

def resolver():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    it = iter(entrada)
    t = int(next(it))  # Número de casos
    for caso in range(1, t + 1):
        n = int(next(it))  # Total de cubículos libres iniciales
        k = int(next(it))  # Posición de la persona a consultar
        # Usamos un max-heap (con números negativos) y un diccionario para agrupar frecuencias
        frecuencias = defaultdict(int)
        frecuencias[n] = 1
        heap = [-n]
        while True:
            actual = -heapq.heappop(heap)
            cantidad = frecuencias.pop(actual)
            # Cada bloque se divide en dos sub-bloques
            izq = actual // 2
            der = (actual - 1) // 2
            # Si la persona k cae dentro de este grupo de bloques
            if k <= cantidad:
                print(f"Case #{caso}: {izq} {der}")
                break
            k -= cantidad
            # Agregar los nuevos intervalos generados
            for nuevo in (izq, der):
                if nuevo > 0:
                    if nuevo not in frecuencias:
                        heapq.heappush(heap, -nuevo)
                    frecuencias[nuevo] += cantidad
if __name__ == "__main__":
    resolver()

