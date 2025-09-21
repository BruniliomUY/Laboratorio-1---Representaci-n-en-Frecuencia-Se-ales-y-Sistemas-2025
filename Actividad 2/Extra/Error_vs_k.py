import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones
def funcion_cuadrada(t, periodo=1.0):
    half_period = periodo / 2
    return np.where((t % periodo) < half_period, 1.0, -1.0)

def funcion_sierra(t, periodo=1.0):
    return 2 * ((t % periodo) / periodo) - 1

# Función para calcular el error de Fourier
def calcular_error_fourier(funcion, T, k_max, nombre_funcion):
    Calcula el error de la serie de Fourier para diferentes valores de k
    """
    # Rango de valores de k a probar
    k_values = np.arange(1, k_max + 1, 2)  # Solo valores impares para mejor convergencia
    errors = []
    
    # Crear arreglo de tiempo para integración
    t_integration = np.linspace(0, T, 1000)
    
    # Crear arreglo de tiempo para evaluación (más amplio)
    t_eval = np.linspace(-T, 2*T, 1000)
    
    print(f"Calculando errores para {nombre_funcion}...")
    
    for k in k_values:
        # Calcular coeficientes de Fourier
        a = np.zeros(k + 1, dtype=complex)
        for n in range(0, k + 1):
            a[n] = 1 / T * np.trapezoid(
                funcion(t_integration, T) * np.exp(-1j * 2 * np.pi * n * t_integration / T), 
                t_integration
            )
        
        # Calcular serie de Fourier
        fourier_sum = a[0] * np.ones_like(t_eval, dtype=complex)
        for n in range(1, k + 1):
            fourier_sum += 2 * a[n] * np.exp(1j * 2 * np.pi * n * t_eval / T)
        
        fourier_sum_real = fourier_sum.real
        
        # Calcular error
        diferencia = funcion(t_eval, T) - fourier_sum_real
        error = (1.0 / T) * np.trapezoid(diferencia**2, t_eval)
        errors.append(error)
        
        if k % 20 == 1:  # Mostrar progreso cada 20 términos
            print(f"  k={k}: error={error:.6f}")
    
    return k_values, np.array(errors)

# Parámetros
T = 3.0
k_max = 10

print("=== ANÁLISIS DE CONVERGENCIA DE SERIES DE FOURIER ===\n")

# Calcular errores para función cuadrada
k_cuadrada, error_cuadrada = calcular_error_fourier(funcion_cuadrada, T, k_max, "Función Cuadrada")

print("\n" + "="*50)

# Calcular errores para función sierra
k_sierra, error_sierra = calcular_error_fourier(funcion_sierra, T, k_max, "Función Sierra")

# Crear gráfico
plt.figure(figsize=(10, 6))

# Gráfico: Error vs k
plt.plot(k_cuadrada, error_cuadrada, 'b-o', label='Función Cuadrada', markersize=5, linewidth=2)
plt.plot(k_sierra, error_sierra, 'r-s', label='Función Sierra', markersize=5, linewidth=2)
plt.xlabel('Número de términos (k)', fontsize=14)
plt.ylabel('Error de convergencia', fontsize=14)
plt.title('Error vs Número de términos', fontsize=16, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.yscale('log')  # Escala logarítmica para mejor visualización

plt.tight_layout()
plt.show()

# Mostrar estadísticas resumidas
print("\n" + "="*60)
print("ESTADÍSTICAS DE CONVERGENCIA")
print("="*60)

print(f"\nFUNCIÓN CUADRADA:")
print(f"  Error inicial (k=1): {error_cuadrada[0]:.6f}")
print(f"  Error final (k={k_cuadrada[-1]}): {error_cuadrada[-1]:.6f}")
print(f"  Mejora: {error_cuadrada[0]/error_cuadrada[-1]:.2f}x")

print(f"\nFUNCIÓN SIERRA:")
print(f"  Error inicial (k=1): {error_sierra[0]:.6f}")
print(f"  Error final (k={k_sierra[-1]}): {error_sierra[-1]:.6f}")
print(f"  Mejora: {error_sierra[0]/error_sierra[-1]:.2f}x")

print(f"\nCOMPARACIÓN:")
print(f"  Error final cuadrada: {error_cuadrada[-1]:.6f}")
print(f"  Error final sierra: {error_sierra[-1]:.6f}")
print(f"  Ratio sierra/cuadrada: {error_sierra[-1]/error_cuadrada[-1]:.2f}x")
