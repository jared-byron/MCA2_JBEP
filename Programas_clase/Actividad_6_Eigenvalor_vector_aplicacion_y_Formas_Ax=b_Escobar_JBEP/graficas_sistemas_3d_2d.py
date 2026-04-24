# Eigenvalor vector aplicacion y Formas Ax=b
# Actividad 6
# Profesores: Roberto Mendez y Antonio Romero 
# Fecha de entrega: 23 abril 2026
# Materia: Matematicas para las Ciencias Aplicadas II 
# Alumno: Escobar Perez Jared Byron

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Gráfica Sistema A (3D - Matriz de Hilbert)
fig = plt.figure(figsize=(12, 5))

# Ecuaciones:
# 1) x + 1/2y + 1/3z = 1   => z = 3(1 - x - 1/2y)
# 2) 1/2x + 1/3y + 1/4z = 0 => z = 4(-1/2x - 1/3y)
# 3) 1/3x + 1/4y + 1/5z = 0 => z = 5(-1/3x - 1/4y)

ax1 = fig.add_subplot(121, projection='3d')
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

Z1 = 3 * (1 - X - 0.5*Y)
Z2 = 4 * (-0.5*X - (1/3)*Y)
Z3 = 5 * (-(1/3)*X - 0.25*Y)

ax1.plot_surface(X, Y, Z1, alpha=0.5, color='red', label='Ec 1')
ax1.plot_surface(X, Y, Z2, alpha=0.5, color='blue', label='Ec 2')
ax1.plot_surface(X, Y, Z3, alpha=0.5, color='green', label='Ec 3')
ax1.set_title('Sistema a) - Planos en 3D')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# Grafica Sistema C (2D - Sistema Inestable)
# Ecuaciones:
# 1) x + 2y = 3            => y = (3 - x) / 2
# 2) 2x + 4.0001y = 6.0001 => y = (6.0001 - 2x) / 4.0001

ax2 = fig.add_subplot(122)
x2_vals = np.linspace(0, 3, 100)
y1_vals = (3 - x2_vals) / 2
y2_vals = (6.0001 - 2*x2_vals) / 4.0001

ax2.plot(x2_vals, y1_vals, 'r-', linewidth=2, label='x + 2y = 3')
ax2.plot(x2_vals, y2_vals, 'b--', linewidth=2, label='2x + 4.0001y = 6.0001')
ax2.set_title('Sistema c) - Lineas casi paralelas')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()

print("NOTA PARA EL INCISO B:")
print("El sistema b) contiene 4 incognitas, lo que representa hiperplanos en R^4.")
print("No es posible graficarlo en un frame estandar de 2D o 3D.")