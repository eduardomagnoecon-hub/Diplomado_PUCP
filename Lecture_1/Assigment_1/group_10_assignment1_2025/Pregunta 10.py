
# Paso 1 Importamos la la libreria numpy con import
import numpy as np

# Paso2 Generar matriz 4x4 con enteros aleatorios entre 1 y 100 como se indica en el ejercicio
matriz = np.random.randint(1, 101, size=(4, 4))
print("Matriz generada:\n", matriz)

# Paso 3 Calculamos la media por columna
media_columnas = np.mean(matriz, axis=0)
print("\nMedia por columna:", media_columnas)

# Paso 4 Calculamos la suma de la diagonal principal
suma_diagonal = np.trace(matriz)
print("\nSuma de la diagonal principal:", suma_diagonal)
