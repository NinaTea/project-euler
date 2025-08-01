# es pd pero en vez de guardar la cantidad de caminos
# hay que guardar la minima suma para una grilla de tama;o i/j

N = 80


def camino_de_minima_suma(n):
    # matriz con resultados previos
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # cantidad de caminos para 1x1
    dp[1][1] = 2

    # los bordes solo suman 1 posible camino mas
    for j in range(2, n + 1):
        dp[1][j] = 1 + dp[1][j-1]

    for i in range(2, n + 1):
        dp[i][1] = 1 + dp[i-1][1]

    # no estoy en ningun borde
    for i in range(2, n + 1):
        for j in range(2, n + 1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[n][n]


if
