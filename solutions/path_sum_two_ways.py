# es pd pero en vez de guardar la cantidad de caminos
# hay que guardar la minima suma para una grilla de tama;o i/j

N = 80
grilla = [[0] * N for _ in range(N)]


def camino_de_minima_suma(n):
    # matriz con resultados previos
    dp = [[0] * N for _ in range(N)]

    # minima suma para una grilla 1x1
    dp[0][0] = grilla[0][0]

    # minimo de los bordes es la acumulada
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + grilla[0][j]

    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + grilla[i][0]

    # no estoy en ningun borde
    for i in range(1, N):
        for j in range(1, N):
            valor = grilla[i][j]
            izq = dp[i][j-1] + valor
            arriba = dp[i-1][j] + valor

            if izq <= arriba:
                dp[i][j] = izq
            else:
                dp[i][j] = arriba

    return dp[N-1][N-1]


if __name__ == "__main__":
    with open("/home/cami/Desktop/en_git_hub/project-euler/0081_matrix.txt") as f:
        contenido = f.read()  # devuelve todo el contenido del archivo en un str gigante
        # cada linea es un elemento del array [str]
        contenido = contenido.split()
        n = 0
        for l in contenido:
            numeros = l.split(",")  # str -> [str]
            numeros = [int(numeros[i]) for i in range(N)]  # [int]

            for j in range(N):
                grilla[n][j] = numeros[j]

            n += 1

    print(camino_de_minima_suma(N))
