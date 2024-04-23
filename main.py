# n = int(input("Введите количество известных пар х,y "))
#
# dict = {}
#
#
# for i in range(n):
#     print(f"Введите пару №{i}:")
#     x, y = map(int, input().split())
#     dict[x] = y

def solve(dict):

    n = len(dict)

    xx = list(map(lambda o: o*o, list(dict)))
    xy = list(map(lambda o: dict[o]*o, list(dict)))
    print(xx)
    print(xy)
    xxsum = sum(xx)
    xysum = sum(xy)
    sumy = sum(list(dict.values()))
    sumx = sum(list(dict))

    a = (n*xysum - sumx*sumy)/(n*xxsum-sumx*sumx)

    b = (sumy*xxsum - sumx*xysum)/(n*xxsum-sumx*sumx)

    print(f"y={a}x+({b})")


solve({
    -2:-11.47,
    -1:-7.59,
    0:-4.32,
    1:-0.41,
    2:3.01,
    3: 6.91,
    4:10.12,
    5:14.08
})