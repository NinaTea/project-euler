"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

"""
from numpy import sqrt, floor

# aca no optimizamos

# ir actualizando el mayor o quedarnos con el inmediato anterior
# a terminar sqrt (600851475143) porque ya sabemos que mayor a eso no va a haber

N = 600851475143


def soy_divisor(a, b):
    return a % b == 0


def es_primo(n):
    raiz = int(floor(sqrt(n)))
    for d in range(2, raiz+1):
        if n % d == 0:
            return False
    return True


def pseudo_factorizar(n):
    maximo = 2
    raiz = int(floor(sqrt(n)))
    for d in range(2, raiz+1):
        if soy_divisor(n, d) and es_primo(d):
            maximo = d

    print(maximo)


pseudo_factorizar(N)
