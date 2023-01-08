def determinant(d1,d2,d3,d4,d5,d6,d7,d8,d9):
    return (d1*d5*d9 + d4*d8*d3 + d7*d2*d6 - d1*d8*d6 - d4*d2*d9 - d7*d5*d3)


l = input().split()
a1 = int(l[0])
a2 = int(l[1])
l= input().split()
b1 = int(l[0])
b2 = int(l[1])
l = input().split()
c1 = int(l[0])
c2 = int(l[1])


m = int(input())

for i in range(m):
    l = input().split()
    d1 = int(l[0])
    d2 = int(l[1])
    d = determinant(a1, a2, a1 * a1 + a2 * a2, c1, c2,c1 * c1 + c2 * c2, d1, d2, d1 * d1 + d2 * d2) + determinant(a1, a2, a1 * a1 + a2 * a2, b1, b2,  b1 * b1 + b2 * b2,  c1, c2, c1 * c1 + c2 * c2) - determinant(b1, b2, b1 * b1 + b2 * b2, c1, c2, c1 *c1 + c2 * c2, d1, d2, d1 * d1 + d2 * d2) - determinant(a1, a2, a1 * a1 + a2 * a2, b1, b2, b1 * b1 + b2 * b2,  d1, d2, d1 * d1 + d2 * d2)
    if d < 0:
      print("OUTSIDE")
    elif d > 0:
      print("INSIDE")
    else:
      print("BOUNDARY")  



