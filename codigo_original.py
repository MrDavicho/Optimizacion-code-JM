import time

# Registramos el tiempo de inicio
inicio = time.time()

# Función para verificar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    i = 3
    while i * i <= numero:
        if numero % i == 0:
            return False
        i += 2
    return True

# Contamos los números primos en el rango
contador_primos = 0
for num in range(1, 100001):
    if es_primo(num):
        contador_primos += 1

# Registramos el tiempo de finalización
fin = time.time()

# Mostramos solo el tiempo de ejecución
print(f"Tiempo de ejecución: {fin - inicio} segundos")
