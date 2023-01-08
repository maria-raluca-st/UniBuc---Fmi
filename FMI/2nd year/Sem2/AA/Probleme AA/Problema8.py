import math

INF = math.inf

xmin = INF
ymin = INF
xmax = -INF 
ymax = -INF

stg = None
drpt = None
top = None
bottom = None

n = int(input())
poligon = []

for i in range(n):
    l = input().split()
    punct = [int(l[0]), int(l[1])]
    poligon.append(punct)

    if punct[0] > xmax:
        drpt = i
        xmax = punct[0]

    if punct[0] < xmin:
        stg = i
        xmin = punct[0]

    if punct[1] < ymin:
        ymin = punct[1]
        bottom = i

    if punct[1] > ymax:
        ymax = punct[1]
        top = i


ok = True
a = stg
while a != drpt and ok == True:
    if poligon[a][0] >= poligon[(a+1) % n][0]:
        ok = False
        break
    a = (a + 1) % n  

while a != stg and ok:
    if poligon[a][0] <= poligon[(a+1) % n][0]:
        ok = False
        break
    a = (a + 1) % n  

if ok == True:
    print("YES")
else:
    print("NO")


ok = True
a = bottom
while a != top and ok:
    if poligon[a][1] >= poligon[(a+1) % n][1]:
        ok = False
        break
    a = (a + 1) % n  


while a != bottom and ok:
    if poligon[a][1] <= poligon[(a+1) % n][1]:
        ok = False
        break
    a = (a + 1) % n  

if ok == True:
    print("YES")
else:
    print("NO")

