def fun(a):
    i=0
    j=-1
    b=[]
    while i<len(a)-3:
        d=a[i]+a[j]
        b.append(d)
        i=i+1
        j=j-1
    print(b)    

fun([5,4,0,1,9])    