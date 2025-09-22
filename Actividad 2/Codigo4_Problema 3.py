import numpy as np
import matplotlib.pyplot as plt

# Parámetros
T = 3.0        # Periodo de la función
k = 5000         # Número de términos de la serie

# Función sierra

def funcion_sierra(t, periodo=T):
    return 2 * ((t % periodo) / periodo) - 1

# Vector de tiempo para el cálculo de coeficientes y error
t_error = np.linspace(0, T, 10*k)  # un solo periodo, muchos puntos para precisión

# Calcular coeficientes de Fourier
a = np.zeros(k + 1, dtype=complex)
for n in range(0, k + 1):
    a[n] = (1/T) * np.trapezoid(funcion_sierra(t_error, T) * np.exp(-1j * 2 * np.pi * n * t_error / T), t_error)

# Suma de Fourier evaluada en t_error (para calcular error)
fourier_sum_error = a[0] * np.ones_like(t_error, dtype=complex)
for n in range(1, k + 1):
    fourier_sum_error += 2 * a[n] * np.exp(1j * 2 * np.pi * n * t_error / T)
fourier_sum_error_real = fourier_sum_error.real

# Función de error
def funcion_error(t, funcion, fourier_real, T=T):
    diferencia = funcion(t, periodo=T) - fourier_real
    error = (1.0 / T) * np.trapezoid(diferencia**2, t)
    return error

# Calcular error correctamente
error = funcion_error(t_error, funcion_sierra, fourier_sum_error_real, T)
print("Error promedio:", error)


# Vector de tiempo para graficar varios periodos
t_graf = np.linspace(-T, 2*T, 10*k)  # 3 periodos

# Suma de Fourier para graficar
fourier_sum_graf = a[0] * np.ones_like(t_graf, dtype=complex)
for n in range(1, k + 1):
    fourier_sum_graf += 2 * a[n] * np.exp(1j * 2 * np.pi * n * t_graf / T)
fourier_sum_graf_real = fourier_sum_graf.real

# Graficar
plt.figure(figsize=(12,5))

# Serie de Fourier vs función original
plt.subplot(1, 2, 1)
plt.plot(t_graf, fourier_sum_graf_real, label="Serie de Fourier")
plt.plot(t_graf, funcion_sierra(t_graf, T), 'r--', label="Función sierra", alpha=0.5)
plt.title(f'Suma de {k} términos de la serie de Fourier')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

# Coeficientes de Fourier
plt.subplot(1, 2, 2)
plt.stem(np.arange(0, 11), np.abs(a[:11]))
plt.title('Coeficientes de la serie de Fourier')
plt.xlabel('n')
plt.ylabel('Amplitud')
plt.grid(True)
plt.tight_layout()

plt.show()
