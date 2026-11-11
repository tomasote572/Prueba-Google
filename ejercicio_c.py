import sys

# EJERCICIO C: Parenting Partnering Returns (Code Jam 2020)
# Tema: Intervalos y Algoritmo Voraz

def resolver():
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    it = iter(entrada)
    t = int(next(it))  # Número de casos
    for caso in range(1, t + 1):
        n = int(next(it))  # Cantidad de actividades
        actividades = []
        for i in range(n):
            inicio = int(next(it))
            fin = int(next(it))
            actividades.append((inicio, fin, i))
        # 1. Ordenamos las actividades por hora de inicio
        actividades.sort(key=lambda x: x[0])
        fin_cameron = 0
        fin_jamie = 0
        asignacion = [''] * n
        posible = True
        # 2. Asignamos cada actividad al primero que esté libre
        for inicio, fin, idx in actividades:
            if inicio >= fin_cameron:
                asignacion[idx] = 'C'
                fin_cameron = fin
            elif inicio >= fin_jamie:
                asignacion[idx] = 'J'
                fin_jamie = fin
            else:
                # Si ninguno está libre, hay conflicto triple
                posible = False
                break
        if posible:
            print(f"Case #{caso}: {''.join(asignacion)}")
        else:
            print(f"Case #{caso}: IMPOSSIBLE")

if __name__ == "__main__":
    resolver()

