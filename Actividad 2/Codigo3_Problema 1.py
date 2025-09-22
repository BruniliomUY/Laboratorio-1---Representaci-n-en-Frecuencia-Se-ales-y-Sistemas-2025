import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Definimos la función periódica de ejemplo (puedes cambiar esta función)
#def ejemplo_funcion_periodica(t):
#    return np.sin(2 * np.pi * t)# + 0.5 * np.sin(4 * np.pi * t)

def funcion_cuadrada(t, periodo=1.0):
    half_period = periodo / 2
    return np.where((t % periodo) < half_period, 1.0, -1.0)

# Parámetros
T = 3.0  # Periodo de la función
k = 5000   # Número de términos a sumar

# Crear un arreglo de tiempo
t = np.linspace(0, T, 10*k)

# Calcular los n primeros coeficientes de la serie de Fourier
a = np.zeros(k + 1, dtype=complex)  # Asegurarse de que el arreglo pueda almacenar valores complejos
for n in range(0, k + 1):
    a[n] = 1 / T * np.trapezoid(funcion_cuadrada(t,T) * np.exp(-1j * 2 * np.pi * n * t / T), t)
    #La función np.trapz realiza la integración numérica usando la regla del trapecio
    #Calculamos los coeficients solo para n>=0, porque para cualquier señal real, los coeficientes negativos son el conjugado de los positivos

# Calcular la serie a partir de los coeficientes, en un intervalo más amplio para ver la periodicidad
t = np.linspace(-T, 2*T, 30*k)
fourier_sum = a[0] * np.ones_like(t, dtype=complex) #Inicializar suma de Fourier con el término n=0
for n in range(1, k + 1):
    fourier_sum += 2*a[n] * np.exp(1j * 2 * np.pi * n * t / T)
    #Nota: en lugar de sumar los valores de n<0 y n>0, sumamos dos veces los valores de n>0
    #Finalmente tomaremos la parte real de la suma, lo que es equivalente a sumar los términos negativos y positivos 

# Modificar esta línea para obtener la parte real de fourier_sum
fourier_sum_real = fourier_sum.real

t_error = np.linspace(0, T, 10*k)

fourier_sum_error = a[0] * np.ones_like(t_error, dtype=complex)
for n in range(1, k + 1):
    fourier_sum_error += 2 * a[n] * np.exp(1j * 2 * np.pi * n * t_error / T)
fourier_sum_error_real = fourier_sum_error.real

#Calcular la convergencia de la serie en bace a la potencia promedio del error
def funcion_error(t_error, funcion_cuadrada, fourier_sum_error_real, T=3):
    # Recalcular la señal cuadrada y la suma de Fourier con el t refinado
    diferencia = funcion_cuadrada(t_error, periodo=T) - fourier_sum_error_real

    # Integral según Oppenheim (Sección 3.4)
    error = (1.0 / T) * np.trapezoid(diferencia**2, t_error)

    return error

print(funcion_error(t_error, funcion_cuadrada, fourier_sum_error_real, T=3.0))

plt.figure(figsize=(10, 5))

# Graficar la parte real de la suma de Fourier
plt.subplot(1, 2, 1)
plt.plot(t, fourier_sum.real)
plt.plot(t, funcion_cuadrada(t,T), 'r--', label='Función Original', alpha=0.5)
plt.title(f'Suma de los primeros {k} términos de la serie de Fourier (Parte Real)')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()

# Graficar los coeficientes de la serie de Fourier
plt.subplot(1, 2, 2)
plt.stem(np.arange(0, 11), np.abs(a[0:11]))
plt.title('Coeficientes de la serie de Fourier')
plt.xlabel('n')
plt.ylabel('Amplitud')
plt.grid(True)
plt.tight_layout()
plt.show()