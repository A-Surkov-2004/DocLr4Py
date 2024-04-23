import AntiMatrix as AM


def cin():
    n = int(input("Введите количество известных пар х,y "))

    dict = {}

    for i in range(n):
        print(f"Введите пару №{i+1}:")
        x, y = map(int, input().split())
        dict[x] = y
    return dict


def conversion(v, stepen):
    vx = [0] * len(v)
    for i in range(len(v)):
        vx[i] = [0] * (stepen + 1)
        for j in range(stepen + 1):
            vx[i][j] = pow(v[i], j)

    return vx


def solve(vx, vy):
    n = len(vx)
    stepen = len(vx[0])

    xtx = [[0 for b in range(stepen)] for a in range(stepen)]
    xty = [0] * stepen

    # print(xtx)
    # print(vx)

    for i in range(stepen):
        for j in range(stepen):
            for k in range(n):
                xtx[i][j] += vx[k][i] * vx[k][j]

    # print(xtx)

    for i in range(stepen):
        for k in range(n):
            xty[i] += vx[k][i] * vy[k]

    # print(xty)
    # print(xtx)

    antixtx = AM.getAntiMatrix(xtx)

    matrixA = [0] * stepen

    # print(antixtx)
    # print(xty)

    for i in range(stepen):
        for k in range(stepen):
            matrixA[i] += antixtx[k][i] * xty[k]
            # print(f'c[{i}][{1}] += {antixtx[k][i]} * {xty[k]}')
        matrixA[i] = round(matrixA[i], 5)

    # print(matrixA)


    eqs = f'y = '
    for j in range(stepen):
        eqs += f'{matrixA[j]}*x^{j} + '
    eqs = eqs[0:len(eqs) - 3]


    print(eqs)


def main():
    d = cin()
    stepen = int(input("Укажите степень полинома: "))
    vx = conversion(list(d), stepen)
    vy = list(d.values())
    solve(vx, vy)


main()

# vx = [[1, 1, 1], [1, 2, 4], [1, 3, 9]]
# vy = [3, 7, 23]
# solve(vx,vy)
