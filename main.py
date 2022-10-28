def disp(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('%-7s' % round(matrix[i][j], 2), end="")
        print()


def mult_vect(vec1, vec2):
    s = 0
    for i in range(len(vec1)):
        s += vec1[i] * vec2[i]
    return s


def mult_vecnum(n, vec):
    temp = [0] * len(vec)
    for i in range(len(vec)):
        temp[i] = vec[i] * n
    return temp


def minus(vec1, vec2):
    temp = [0] * len(vec1)
    for i in range(len(vec1)):
        temp[i] = vec1[i] - vec2[i]
    return temp


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

    return X


def ort(SLAU):
    SIZE = len(SLAU)
    a = []
    T = []
    R = []

    for i in range(SIZE):
        temp = []
        for j in range(SIZE):
            temp.append(0)
        T.append(temp)

    for i in range(SIZE + 1):
        temp = []
        for j in range(SIZE):
            temp.append(SLAU[j][i])
        a.append(temp)

    R.append(a[0])
    for i in range(SIZE - 1):
        T[i][i] = 1
        for j in range(i + 1, SIZE):
            T[i][j] = mult_vect(R[i], a[j]) / mult_vect(R[i], R[i])
        temp = a[i + 1]
        for j in range(i + 1):
            temp = minus(temp, mult_vecnum(T[j][i + 1], R[j]))
        R.append(temp)

    X = [0] * SIZE
    for i in range(SIZE - 1, -1, -1):
        X[i] = mult_vect(R[i], a[SIZE]) / mult_vect(R[i], a[i])
        a[SIZE] = minus(a[SIZE], mult_vecnum(X[i], a[i]))

    for i in range(SIZE):
        X[i] = round(X[i], 2)

    return X


SLAU = [
    [9, 8, 3, 4],
    [3, 6, 3, -3],
    [5, 3, 1, 2]
]
print("gauss: ", gauss(SLAU))
SLAU = [
    [9, 8, 3, 4],
    [3, 6, 3, -3],
    [5, 3, 1, 2]
]
print("ort: ", ort(SLAU))
