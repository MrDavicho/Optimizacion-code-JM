import time
import math

inicio = time.time()

def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    limite = int(math.sqrt(numero)) + 1
    for i in range(3, limite, 2):
        if numero % i == 0:
            return False
    return True

contador_primos = sum(1 for num in range(1, 100001) if es_primo(num))

fin = time.time()
print(f"Tiempo de ejecución: {fin - inicio} segundos")
