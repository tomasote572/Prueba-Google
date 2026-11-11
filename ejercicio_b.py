import sys

# EJERCICIO B: Moons and Umbrellas (Code Jam 2021)
# Tema: Programación Dinámica

def resolver():
    lineas = sys.stdin.read().splitlines()
    if not lineas:
        return
    # Leer casos válidos ignorando líneas vacías
    casos = [l.strip() for l in lineas if l.strip()]
    if not casos:
        return
    t = int(casos[0])
    inf = float('inf')
    for caso in range(1, t + 1):
        partes = casos[caso].split()
        costo_cj = int(partes[0])  # Costo por la subsecuencia CJ
        costo_jc = int(partes[1])  # Costo por la subsecuencia JC
        mural = partes[2]          # Cadena con C, J y ?
        # Programación dinámica: costo mínimo terminando en 'C' o 'J'
        costo_c = inf
        costo_j = inf
        for i, ch in enumerate(mural):
            nuevo_c = inf
            nuevo_j = inf
            if i == 0:
                # Caso base: primer carácter
                if ch != 'J':
                    nuevo_c = 0
                if ch != 'C':
                    nuevo_j = 0
            else:
                # Transiciones para el carácter actual
                if ch != 'J':
                    nuevo_c = min(costo_c, costo_j + costo_jc)
                if ch != 'C':
                    nuevo_j = min(costo_j, costo_c + costo_cj)
            costo_c = nuevo_c
            costo_j = nuevo_j
        respuesta = min(costo_c, costo_j)
        print(f"Case #{caso}: {respuesta}")
if __name__ == "__main__":
    resolver()

