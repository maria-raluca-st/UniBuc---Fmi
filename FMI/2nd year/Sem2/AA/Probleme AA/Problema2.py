

def determinant():
    return xq*yr + xp*yq + yp*xr - xq*yp - xr*yq - yr*xp

n = int(input())
l = 0
r = 0
to = 0
v = []

for i in range (1,n+1) :
    li = input()
    li = li.split()

    x = int(li[0])
    y = int(li[1])
    v.append([x,y])
  
for e in range(len(v)) :
    if e+2 < len(v):
     xp = v[e][0]
     yp = v[e][1]
     xq = v[e+1][0]
     yq = v[e+1][1]
     xr = v[e+2][0]
     yr = v[e+2][1]
     if determinant() == 0:
        to += 1
     elif determinant() < 0:
        r += 1
     else:
        l += 1

xp = v[len(v) - 2][0]
yp = v[len(v) - 2][1]
xq = v[len(v) - 1][0]
yq = v[len(v) - 1][1]
xr = v[0][0]
yr = v[0][1]
if determinant() == 0:
    to += 1
elif determinant() < 0:
    r += 1
else:
    l += 1

print(l ,r, to)

    

    
