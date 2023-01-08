def determinant(xp , yp , xq , yq , xr , yr):
    return xq*yr + xp*yq + yp*xr - xq*yp - xr*yq - yr*xp


def graham_scan_inf(p):
    l = [p[0], p[1]]
    for i in range(2, len(p)):
        l.append(p[i])
        while len(l) > 2 and determinant(l[-3][0] , l[-3][1], l[-2][0] ,l[-2][1] , l[-1][0] , l[-1][1]) < 0:
            l.pop(-2)
    return l


def graham_scan_sup(p):
    l = [p[0], p[1]]
    for i in range(2, len(p)):
        l.append(p[i])
        while len(l) > 2 and determinant(l[-3][0] , l[-3][1], l[-2][0] ,l[-2][1] , l[-1][0] , l[-1][1]) > 0:
            l.pop(-2)
    return l


def graham_scan(p):
    p.sort(key=lambda point: point[0])
    p.sort(key=lambda point: point[1])
    inferior = graham_scan_inf(p)

    p.sort(key=lambda point: point[0])
    p.sort(key=lambda point: point[1])
    superior = graham_scan_sup(p)

    return inferior + superior


nr_p = int(input())
points = []

for index in range(nr_p):
    inp = input().split()
    points.append((int(inp[0]), int(inp[1]), index))


puncte_finale = graham_scan(points)

puncte_finale.sort(key=lambda punct: (punct[2]))

list_p = []
for i in range(len(puncte_finale)):
    if puncte_finale[i] not in list_p:
        list_p.append(puncte_finale[i])


print(len(list_p))
for p in list_p:
    print(p[0], p[1])