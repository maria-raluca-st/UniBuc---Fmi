import cmath


def is_P_InSegment_P0P1(P, P0,P1):
    p0 = P0[0]- P[0], P0[1]- P[1]
    p1 = P1[0]- P[0], P1[1]- P[1]


    det = (p0[0]*p1[1] - p1[0]*p0[1])
    prod = (p0[0]*p1[0] + p0[1]*p1[1])
    
    return (det == 0 and prod < 0) or (p0[0] == 0 and p0[1] == 0) or (p1[0] == 0 and p1[1] == 0)


def isInsidePolygon(P , Vertices ):


    sum_ = complex(0,0)


    for i in range(1, len(Vertices) + 1):
        v0, v1 = Vertices[i-1] , Vertices[i%len(Vertices)]


        if is_P_InSegment_P0P1(P,v0,v1):
            return -1


        sum_ += cmath.log( (complex(*v1) - complex(*P)) / (complex(*v0) - complex(*P)) )


    return abs(sum_) > 1



poligon_pct = []
puncte_de_verificat = []
n = int(input())

b = "BOUNDARY"
ins = "INSIDE"
o = "OUTSIDE"

for i in range(1,n+1):
    l = input().split()
    p = [int(l[0]), int(l[1])]
    poligon_pct.append(p)

m = int(input())

for i in range(m):
    l = input().split()
    p = [float(l[0]), float(l[1])]
    puncte_de_verificat.append(p)


for p in puncte_de_verificat:
    if isInsidePolygon(p, poligon_pct):
        if isInsidePolygon(p, poligon_pct) == -1:
            print(b)
        else:
            print(ins)
    else:
        print(o)

