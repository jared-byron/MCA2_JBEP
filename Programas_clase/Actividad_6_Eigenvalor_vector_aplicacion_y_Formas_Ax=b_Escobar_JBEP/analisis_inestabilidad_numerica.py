# Eigenvalor vector aplicacion y Formas Ax=b
# Actividad 6
# Profesores: Roberto Mendez y Antonio Romero 
# Fecha de entrega: 23 abril 2026
# Materia: Matematicas para las Ciencias Aplicadas II 
# Alumno: Escobar Perez Jared Byron

import numpy as np

print("="*50)
print(" MATRIZ DE VANDERMONDE 4x4 - Ejercicio 2.2 b)")
print("="*50)

# 1. Definir la matriz A original
A = np.array([
    [1,       1,       1,       1      ],
    [1.01,    1.02,    1.03,    1.04   ],
    [1.01**2, 1.02**2, 1.03**2, 1.04**2],
    [1.01**3, 1.02**3, 1.03**3, 1.04**3]
])

# 2. Calcular la matriz inversa A^-1
A_inv = np.linalg.inv(A)

print("\n--- Matriz Inversa (A^-1) ---")
print("Observa como los numeros explotan en millones por la inestabilidad:")
print(np.round(A_inv, 2))

# 3. Calcular la norma L_infinito (Suma máxima de filas)
# En numpy, el parámetro np.inf le indica que calcule la norma infinito
norma_A = np.linalg.norm(A, np.inf)
norma_A_inv = np.linalg.norm(A_inv, np.inf)

print("\n--- Normas L_infinito ---")
print(f"Norma ||A||_inf: {norma_A:.4f}")
print(f"Norma ||A^-1||_inf: {norma_A_inv:,.2f}")

# 4. Calcular el número de condición
kappa_inf = norma_A * norma_A_inv

print("\n--- Numero de Condición ---")
print(f"Condicion k(A): {kappa_inf:,.2f}")

# Comprobacion directa con la funcion nativa de condición de numpy
kappa_numpy = np.linalg.cond(A, np.inf)
print(f"Condicion k(A) directa con numpy: {kappa_numpy:,.2f}")

if kappa_inf > 1:
    print("\nCONCLUSION: k(A) >> 1, el sistema esta severamente mal condicionado.")