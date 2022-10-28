def disp(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('%-7s' % round(matrix[i][j], 2), end="")
        print()

SLAU = [
    [9, 8, 3, 4],
    [3, 6, 3, -3],
    [5, 3, 1, 2]
]

def gauss(SLAU):
    SIZE = len(SLAU)
    disp(SLAU)

    # Вся магия происходит тут
    for i in range(SIZE):
        SLAUii = SLAU[i][i]
        line = []
        for j in range(i + 1, SIZE):
            line.append(SLAU[j][i])
        for j in range(i, SIZE + 1):
            SLAU[i][j] /= SLAUii
            for k in range(i + 1, SIZE):
                SLAU[k][j] -= line[(k - 1 + len(line)) % len(line)] * SLAU[i][j] / SLAU[i][i]
        # disp(SLAU)

    # Подсчет иксов
    X = [0] * SIZE
    for i in range(SIZE - 1, -1, -1):
        s = 0
        for j in range(i + 1, SIZE):
            s += SLAU[i][j] * X[j]
        X[i] = SLAU[i][SIZE] - s

    for i in range(SIZE):
        X[i] = round(X[i], 2)

    print(X)


gauss(SLAU)
