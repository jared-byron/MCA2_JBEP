# Eigenvalor vector aplicacion y Formas Ax=b
# Actividad 6
# Profesores: Roberto Mendez y Antonio Romero 
# Fecha de entrega: 23 abril 2026
# Materia: Matematicas para las Ciencias Aplicadas II 
# Alumno: Escobar Perez Jared Byron

import numpy as np
from sympy import Matrix

# INCISO A: Matriz de Hilbert (3x3)
print("="*50)
print(" INCISO A: MATRIZ DE HILBERT ")
print("="*50)

# 1. Cálculo con numpy (Numérico)
A_a_np = np.array([
    [1,   1/2, 1/3],
    [1/2, 1/3, 1/4],
    [1/3, 1/4, 1/5]
])

eigenvalores_a, eigenvectores_a = np.linalg.eig(A_a_np)
print("\n--- 1. Eigenvalores y Eigenvectores con numpy ---")
print("Eigenvalores:\n", eigenvalores_a)
print("Eigenvectores unitarios:\n", eigenvectores_a)

# 2. Calculo con sympy
A_a_sym = Matrix([
    [1,   1/2, 1/3],
    [1/2, 1/3, 1/4],
    [1/3, 1/4, 1/5]
])

eigen_data_a = A_a_sym.eigenvects()
print("\n--- 2. Eigenvalores y Eigenvectores con sympy ---")
for i, (val, mult, vecs) in enumerate(eigen_data_a):
    # Usamos evalf(5) para no imprimir la expresion irracional gigante de Cardano
    print(f"\nEl Eigenvalor {i+1} es aprox: {val.evalf(5)}") 
    for j, vec in enumerate(vecs):
        # Convertimos a lista de floats para facilitar la lectura
        vec_float = [float(v.evalf(5)) for v in vec]
        print(f"  Un eigenvector de este valor es: {vec_float}")


# INCISO B: Matriz de Vandermonde (4x4)
print("\n\n" + "="*50)
print(" INCISO B: MATRIZ DE VANDERMONDE ")
print("="*50)

# Para esta matriz, al tener potencias de decimales 
A_b_np = np.array([
    [1,       1,       1,       1      ],
    [1.01,    1.02,    1.03,    1.04   ],
    [1.01**2, 1.02**2, 1.03**2, 1.04**2],
    [1.01**3, 1.02**3, 1.03**3, 1.04**3]
])

eigenvalores_b, eigenvectores_b = np.linalg.eig(A_b_np)
print("\n--- 1. Eigenvalores y Eigenvectores con numpy ---")
print("Eigenvalores:\n", eigenvalores_b)
print("Eigenvectores unitarios:\n", eigenvectores_b)