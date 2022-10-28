def disp(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('%-7s' % matrix[i][j], end="")
        print()


SLAU = [
    [1, -2, 1, 0],
    [2, 2, -1, 3],
    [4, -1, 1, 5]
]

SIZE = len(SLAU)
disp(SLAU)

for i in range(SIZE):
    print()
    SLAUii = SLAU[i][i]
    line = []
    for j in range(i + 1, SIZE):
        line.append(SLAU[j][i])
    for j in range(i, SIZE + 1):
        SLAU[i][j] /= SLAUii
        for k in range(i + 1, SIZE):
            SLAU[k][j] -= line[(k - 1 + len(line)) % len(line)] * SLAU[i][j] / SLAU[i][i]
    disp(SLAU)

X = [0] * SIZE
print(X)
for i in range(SIZE - 1, -1, -1):
    s = 0
    for j in range(i, SIZE - 1):
        s += SLAU[i][j] * X[j]
    X[i] = SLAU[i][SIZE] - s

print(X)
