

def determinant():
    return xq*yr + xp*yq + yp*xr - xq*yp - xr*yq - yr*xp

t = int(input())
l = "LEFT"
r = "RIGHT"
to = "TOUCH"

for i in range (1,t+1) :
    li = input()
    li = li.split()
    xp = int(li[0])
    yp = int(li[1])
    xq = int(li[2])
    yq = int(li[3])
    xr = int(li[4])
    yr = int(li[5])
    if determinant() == 0:
        print(to)
    elif determinant() < 0:
        print (r)
    else:
        print(l)
    

    
