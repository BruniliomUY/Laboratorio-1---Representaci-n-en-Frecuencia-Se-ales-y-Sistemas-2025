import cmath
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin

def suma_parcial_fourier(t, f0, N):
    suma_total = 2/3
    for k in range(-N, N + 1):
        if k % 3 == 0:
            a_k = 0
        elif k != 0:
            a_k =(2*(cmath.exp(-k*(1/3)*pi*1j))*(sin(k*(1/3)*pi)))/(k*pi)
        suma_total += a_k * cmath.exp(2*pi*k*f0*t*1j)
    return suma_total

def señal_original(t):
    """
    Función de la señal original (pulso periódico)
    Para t en [0, 1): valor = 2
    Para t en [1, 3): valor = 0
    Período = 3
    """
    t_mod = t % 3  # Tomar la parte fraccionaria para el período
    if 0 <= t_mod < 1:
        return 2
    else:
        return 0

#para t = 0.5
print("Para t = 0.5:")
for N in [10, 100, 1000, 10000]:
    print(f"Suma parcial para N={N}: {abs(suma_parcial_fourier(0.5, 1/3, N))}")

#para t = 1
print("\nPara t = 1:")
for N in [10, 100, 1000, 10000]:
    print(f"Suma parcial para N={N}: {abs(suma_parcial_fourier(1, 1/3, N))}")

#para t = 1.5
print("\nPara t = 1.5:")
for N in [10, 100, 1000, 10000]:
    print(f"Suma parcial para N={N}: {abs(suma_parcial_fourier(1.5, 1/3, N))}")

#para t = 2
print("\nPara t = 2:")
for N in [10, 100, 1000, 10000]:
    print(f"Suma parcial para N={N}: {abs(suma_parcial_fourier(2, 1/3, N))}")

#para t = 2.5
print("\nPara t = 2.5:")
for N in [10, 100, 1000, 10000]:
    print(f"Suma parcial para N={N}: {abs(suma_parcial_fourier(2.5, 1/3, N))}")

# Generar gráfica con 3 períodos completos
print("\nGenerando gráfica...")

# Parámetros
f0 = 1/3  # Frecuencia fundamental
T = 1/f0  # Período = 3
t_inicio = 0
t_final = 3 * T  # 3 períodos completos
puntos = 1000

# Generar valores de tiempo equiespaciados
t = np.linspace(t_inicio, t_final, puntos)

# Calcular señal original 
y_original = [señal_original(ti) for ti in t]

# Calcular aproximaciones de Fourier para diferentes N
valores_N = [3, 5, 10, 100]
y_fourier = {}

for N in valores_N:
    y_fourier[N] = []
    for ti in t:
        resultado = suma_parcial_fourier(ti, f0, N)
        y_fourier[N].append(resultado.real)

# Crear la gráfica
plt.figure(figsize=(12, 8))

# Señal original
plt.plot(t, y_original, 'k-', linewidth=2, label='Señal Original')

# Aproximaciones de Fourier
colores = ['red', 'blue', 'green', 'orange']
for i, N in enumerate(valores_N):
    plt.plot(t, y_fourier[N], color=colores[i], linewidth=1.5, 
             label=f'Fourier N={N}')

plt.xlabel('Tiempo (t)')
plt.ylabel('Amplitud')
plt.title('Señal Original vs Aproximaciones de Fourier\n(3 períodos completos)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(t_inicio, t_final)

# Añadir líneas verticales para marcar los períodos
for i in range(4):  # 0, 1, 2, 3 períodos
    plt.axvline(x=i*T, color='gray', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

print("Gráfica generada exitosamente!")







