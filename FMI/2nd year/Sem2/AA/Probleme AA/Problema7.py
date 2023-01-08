import math

INF = math.inf

def intersectie_planuri(P, Q):
    xmax = -math.inf
    xmin = math.inf
    ymin = math.inf
    ymax = -math.inf
    for p in P:
        if p[1] == 0:
            if p[0]*Q[0]+ p[2]>=0:
                continue
            d = -p[2] / p[0]
            if d > Q[0]:
                xmin = min(xmin, d)

            else:
                xmax = max(xmax, d)
        else:
            if p[1]*Q[1]+ p[2]>=0:
                continue
            d = -p[2] / p[1]
            if d > Q[1]:
                ymin = min(ymin, d)

            else:
                ymax = max(ymax, d)

    if max(xmin, ymin) == INF or min(xmax, ymax) == -INF:
        return 0
    return (xmax-xmin)*(ymax-ymin)


n = int(input())

lista_p = []

for i in range(n):
    p = input().split()
    elem_p = [int(p[0]), int(p[1]), int(p[2])]
    lista_p.append(elem_p)

n = int(input())

for i in range(n):
    punct = input().split()
    punct = [float(punct[0]), float(punct[1])]
    valid = intersectie_planuri(lista_p, punct)
    if valid == 0:
        print("NO")
    else:
        print("YES")
        print("{:.6f}".format(valid))
