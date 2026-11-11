import sys

# EJERCICIO A: d1000000 (Code Jam 2022)
# Tema: Ordenamiento y Algoritmo Voraz (Greedy)

def resolver():
    # Leer toda la entrada estándar
    entrada = sys.stdin.read().split()
    if not entrada:
        return
    it = iter(entrada)
    t = int(next(it))  # Número de casos de prueba
    for caso in range(1, t + 1):
        n = int(next(it))  # Cantidad de dados
        # Caras de cada dado
        dados = [int(next(it)) for _ in range(n)]
        # 1. Ordenamos los dados de menor a mayor cantidad de caras
        dados.sort()
        # 2. Construimos la escalera de números (1, 2, 3...) de forma voraz
        escalera = 0
        for dado in dados:
            if dado > escalera:
                escalera += 1
        # Imprimir salida en el formato requerido
        print(f"Case #{caso}: {escalera}")

if __name__ == "__main__":
    resolver()

