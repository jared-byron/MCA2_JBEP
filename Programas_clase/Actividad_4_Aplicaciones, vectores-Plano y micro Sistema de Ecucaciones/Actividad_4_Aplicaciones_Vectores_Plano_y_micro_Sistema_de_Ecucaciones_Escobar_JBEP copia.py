# Aplicaciones, vectores-Plano y micro Sistema de Ecucaciones
# Actividad 4
# Profesores: Roberto Mendez y Antonio Romero 
# Fecha de entrega: 13 abril 2026
# Materia: Matematicas para las Ciencias Aplicadas II 
# Alumno: Escobar Perez Jared Byron

import numpy as np
import math

# APLICACION REAL DEL PCM Y DLT (AACTIVIDAD 1)
# 1. DATOS REALES (Caja de UNO No Mercy)
puntos_3D = np.array([
    [0, 0, 0], [11.6, 0, 0], [0, 3.8, 0], 
    [11.6, 3.8, 0], [11.6, 3.8, 9.2], [0, 3.8, 9.2]
])

puntos_2D = np.array([
    [1045, 5320], [2540, 6420], [960, 4800], 
    [2610, 5840], [3180, 4610], [1420, 3960]
])

# 2. CONSTRUCCION DE LA MATRIZ A

A = []
for i in range(len(puntos_3D)):
    X, Y, Z = puntos_3D[i]
    u, v = puntos_2D[i]
    A.append([X, Y, Z, 1, 0, 0, 0, 0, -u*X, -u*Y, -u*Z, -u])
    A.append([0, 0, 0, 0, X, Y, Z, 1, -v*X, -v*Y, -v*Z, -v])
A = np.array(A)

# 3. RESOLUCION MATEMATICA PASO A PASO
print("--- Resolviendo sistema Ap = 0 por minimos cuadrados ---")

M = np.dot(A.T, A)

valores_propios, vectores_propios = np.linalg.eigh(M)


vector_solucion = vectores_propios[:, 0]

Matriz_P = vector_solucion.reshape(3, 4)

Matriz_P = Matriz_P / Matriz_P[2, 3]

# 4. RESULTADOS
print("\nMatriz de Proyección P (Método Desglosado):")
print(np.round(Matriz_P, 4))

#APLICACION DEL ALGORITMO RSA (ACTIVIDAD 2.1)

def generate_rsa():
    p, q = 347, 349
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 1009
    
    # Calculamos d usando pow() de Python que implementa Euclides Extendido
    d = pow(e, -1, phi)
    
    print(f"Módulo n: {n}")
    print(f"Phi(n): {phi}")
    print(f"Exponente público e: {e}")
    print(f"Exponente privado d: {d}")
    print(f"Verificación (e*d % phi): {(e*d) % phi}")

if __name__ == "__main__":
    generate_rsa()