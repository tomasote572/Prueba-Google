# Prueba Google · Code Jam · Hackatón Individual (Python)

Repositorio con las soluciones en **Python** para los 5 problemas de algoritmia inspirados en Google Code Jam. Utiliza un único archivo de entrada `entrada.txt` para copiar, pegar y procesar directamente los casos del concurso, mostrando los resultados en consola.

---

## 📁 Archivos del Proyecto

| Archivo | Problema | Descripción Algorítmica |
| :--- | :--- | :--- |
| `Prueba Google · Code Jam · Hackatón individual.html` | — | Enunciados interactivos y generador de entradas oficiales. |
| `entrada.txt` | — | **Archivo único de entrada**: aquí pegas lo que copias del HTML. |
| `ejercicio_a.py` | **A** · d1000000 | Ordenamiento y algoritmo voraz de dados. |
| `ejercicio_b.py` | **B** · Moons and Umbrellas | Programación dinámica para minimizar costo de mural. |
| `ejercicio_c.py` | **C** · Parenting Partnering Returns | Intervalos y asignación voraz sin solapamiento. |
| `ejercicio_d.py` | **D** · Chain Reactions | Árboles y algoritmo voraz bottom-up (DFS). |
| `ejercicio_e.py` | **E** · Bathroom Stalls | Simulación eficiente con números grandes ($10^{18}$) y heap. |

---

## 🚀 Paso a Paso: Cómo Usarlo

### Paso 1: Abrir el HTML y generar tu entrada
1. Abre con doble clic el archivo **`Prueba Google · Code Jam · Hackatón individual.html`** en tu navegador.
2. En la parte superior, escribe tu **Nombre** y **Código** para desbloquear la sesión.
3. Selecciona la pestaña del ejercicio que vas a resolver (**A, B, C, D o E**).
4. En el recuadro **"Tu entrada oficial"**, haz clic en el botón **Copiar**.

---

### Paso 2: Pegar en `entrada.txt`
1. Abre el archivo **`entrada.txt`** en VS Code.
2. Borra lo que tenga, pega la entrada copiada y **guarda el archivo (`Ctrl + S`)**.

---

### Paso 3: Ejecutar el ejercicio y ver el resultado en consola
Abre una terminal de PowerShell en esta carpeta y corre el comando correspondiente:

* **Para el Ejercicio A:**
  ```powershell
  Get-Content entrada.txt | python ejercicio_a.py
  ```

* **Para el Ejercicio B:**
  ```powershell
  Get-Content entrada.txt | python ejercicio_b.py
  ```

* **Para el Ejercicio C:**
  ```powershell
  Get-Content entrada.txt | python ejercicio_c.py
  ```

* **Para el Ejercicio D:**
  ```powershell
  Get-Content entrada.txt | python ejercicio_d.py
  ```

* **Para el Ejercicio E:**
  ```powershell
  Get-Content entrada.txt | python ejercicio_e.py
  ```

La respuesta aparecerá directamente en pantalla en el formato oficial:
```text
Case #1: ...
Case #2: ...
```

---

## 💡 Consejo Útil

Si en alguna terminal de PowerShell te sale el aviso de que no se encuentra Python (debido a ventanas abiertas antes de la instalación), abre una **terminal nueva** (`Ctrl + Shift + \`` en VS Code) o ejecuta:

```powershell
$env:Path = "$env:LOCALAPPDATA\Programs\Python\Python312;$env:Path"
```
