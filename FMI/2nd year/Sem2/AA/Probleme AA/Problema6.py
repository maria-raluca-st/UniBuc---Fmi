import math

xmax = -math.inf
xmin = math.inf
ymax = math.inf
ymin = -math.inf

n = int(input())

lista_p = []

for i in range(n):
    p = input()
    p = p.split()
    elem_p = [int(p[0]), int(p[1]), int(p[2])]
    lista_p.append(elem_p)

for p in lista_p:
    if (p[1] == 0) :
        d = -p[2]/p[0]
        if p[0] > 0:
            xmin = min(xmin, d)
        else:
            xmax = max(xmax, d)
    else:
        d = -p[2]/p[1]
        if p[1] > 0:
            ymax = min(ymax, d)
        else:
            ymin = max(ymin, d)

if (xmax > xmin or ymax < ymin):
    print("VOID")
else:
    if (xmax != -math.inf and xmin != math.inf and ymin != - math.inf and ymax != math.inf):
        print("BOUNDED")
    else:
        print("UNBOUNDED")
