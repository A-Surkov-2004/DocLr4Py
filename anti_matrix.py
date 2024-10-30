def getAntiMatrix(v):

    """
    Получает обратную матрицу от заданной

    Args:
        v (list[list]): Исходная матрица

    Returns:
        list[list]: Обратная матрица
    """

    n = len(v)

    edin = [0] * n
    for i in range(n):
        edin[i] = [0] * n
        edin[i][i] = 1

    for i in range(n):
        for j in range(n):
            v[i].append(edin[i][j])

    n = len(v)

    for i in range(n):
        for j in range(n):
            if j != i:
                try:
                    templine = list(map(lambda num: round(num * v[j][i] / v[i][i], 8), v[i]))
                except ZeroDivisionError as e:
                    templine = [0] * n*2
                for k in range(n*2):
                    v[j][k] = round(v[j][k] - templine[k], 8)

    for i in range(n):
        v[i] = list(map(lambda num: round(num / v[i][i], 8), v[i]))



    #prnt(v,n)

    ans = [0]*n
    for i in range(n):
        ans[i] = v[i][n:n*2]

    #prnt(ans,n)

    return ans


v = [[1,2,3,4,1,0,0,0],
     [4,2,1,5,0,1,0,0],
     [3,5,4,2,0,0,1,0],
     [4,5,2,1,0,0,0,1]]

#print(getAntiMatrix(v))