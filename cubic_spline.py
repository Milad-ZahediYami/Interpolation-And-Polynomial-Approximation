from __future__ import division

def cubic_spline(x,fu, n):
    y = [0] * (n)
    for i in range(0,n):
        y[i] = fu(x[i])
    
    hi = [0] * (n)
    li = [0] * (n)
    ui = [0] * (n)
    zi = [0] * (n)
    ci = [0] * (n)
    bj = [0] * (n)
    dj = [0] * (n)
    alphai = [0] * (n)
    
    for i in range(0, n-1):
        hi[i] = x[i+1] - x[i]
    for i in range(1, n-1):
        alphai[i] = ((3/hi[i])*(y[i+1]-y[i])) - ((3/(hi[i-1]))*(y[i]-y[i-1]))
    li[0] = 1
    ui[0] = 0
    zi[0] = 0

    for i in range(1, n-1):
        li[i] = (2*(x[i+1]-x[i-1])) - (hi[i-1] * ui[i-1])
        ui[i] = hi[i]/li[i]
        zi[i] = (alphai[i]-hi[i-1]-zi[i-1])/li[i]

    li[n-1] = 1
    zi[n-1] = 0
    ci[n-1] = 0
    for j in range(n-2, -1,-1):
        ci[j] = zi[j] - (ui[j]*ci[j+1])
        bj[j] = ((y[j+1] - y[j])/hi[j]) - ((hi[j]*(ci[i+1]+(2*ci[j])))/3)
        dj[j] = (ci[j+1]-ci[j]) / (3*hi[j])
    print("aj         bj         cj         dj         ")
    for i in range(0, n):
        print("%4.4f    %4.4f    %4.4f    %4.4f" % (y[i], bj[i], ci[i], dj[i]))

def f1(x):
    t = (1+x**2)
    n =  1/t
    return n

if __name__ == '__main__':
    cubic_spline([-2,-1,1,2],f1,4)
