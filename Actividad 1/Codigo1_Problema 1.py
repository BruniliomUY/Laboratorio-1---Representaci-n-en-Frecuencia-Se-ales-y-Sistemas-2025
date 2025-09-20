import mpmath as mp

# Configurar precisión alta
mp.mp.dps = 3020
# Configuraciones de visualización de mpmath
mp.mp.pretty = True  # Formato más legible (esta SÍ existe)

# Ejemplo 1: Calcular para diferentes valores de N
print("=== EJEMPLO 1 ===")
lista_total_1 = []
for N_val in [10, 100, 1000, 10000]:
    suma_temp = mp.mpf(0)
    for k in range(-N_val, N_val + 1):
        if k >= 0:
            b_k = mp.mpf(1) / mp.mpf(2 ** k)
        else:
            b_k = mp.mpf(0)
        suma_temp += b_k
    suma_temp = suma_temp - mp.mpf(2)
    lista_total_1.append(suma_temp)
    print(f"N={N_val}: {mp.nstr(suma_temp, 20)}")

print(f"\nΔN(10,100): {mp.nstr(lista_total_1[1] - lista_total_1[0], 20)}")
print(f"ΔN(100,1000): {mp.nstr(lista_total_1[2] - lista_total_1[1], 20)}")
print(f"ΔN(1000,10000): {mp.nstr(lista_total_1[3] - lista_total_1[2], 20)}")

# Ejemplo 2: Calcular para diferentes valores de N
print("\n=== EJEMPLO 2 ===")
lista_total_2 = []

for N_val in [10, 100, 1000, 10000]:
    suma_temp = mp.mpf(0)
    for k in range(-N_val, N_val + 1):
        if k < 0:
            b_k = mp.mpf(0.2) ** (-k)
        else:
            b_k = mp.mpf(0)
        suma_temp += b_k
    suma_temp = suma_temp - mp.mpf(0.25)
    lista_total_2.append(suma_temp)
    print(f"N={N_val}: {mp.nstr(suma_temp, 20)}")

print(f"\nΔN(10,100): {mp.nstr(lista_total_2[1] - lista_total_2[0], 20)}")
print(f"ΔN(100,1000): {mp.nstr(lista_total_2[2] - lista_total_2[1], 20)}")
print(f"ΔN(1000,10000): {mp.nstr(lista_total_2[3] - lista_total_2[2], 20)}")

# Ejemplo 3: Calcular para diferentes valores de N
print("\n=== EJEMPLO 3 ===")
lista_total_3 = []

for N_val in [10, 100, 1000, 10000]:
    suma_temp = mp.mpf(0)
    for k in range(-N_val, N_val + 1):
        if k != 0:
            b_k = -((-1)**k) / abs(k)
        else:
            b_k = mp.mpf(0)
        suma_temp += b_k
    lista_total_3.append(suma_temp)
    print(f"N={N_val}: {mp.nstr(suma_temp, 20)}")

print(f"\nΔN(10,100): {mp.nstr(lista_total_3[1] - lista_total_3[0], 20)}")
print(f"ΔN(100,1000): {mp.nstr(lista_total_3[2] - lista_total_3[1], 20)}")
print(f"ΔN(1000,10000): {mp.nstr(lista_total_3[3] - lista_total_3[2], 20)}")