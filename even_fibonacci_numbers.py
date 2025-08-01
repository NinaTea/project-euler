# queremos la suma de los numeros de la sucesion de fibonacci
# menores a 4 millones y que sean pares
# por la complejidad hago fibonacci iterativo
# los primeros numeros de la sucesion nos dicen que es 1,2,3,5

suma = 2
fib_ultimo = 2
fib_ante_ultimo = 1

cota = 4_000_000
for _ in range(0, cota):
    fib_actual = fib_ultimo + fib_ante_ultimo
    if fib_actual > cota:
        break
    if fib_actual % 2 == 0:
        suma += fib_actual

    fib_ante_ultimo = fib_ultimo
    fib_ultimo = fib_actual
