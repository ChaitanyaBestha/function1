def fun(a):
    i=-1
    b=[]
    while i>=-len(a):
        j=i
        sum=0
        while j>=i:
            sum=sum+a[i][j]
            j=j-1
        b.append(sum)
        i=i-1
    # print(b)
    i=-1
    c=[]
    while i>=-len(b):
        c.append(b[i])
        i=i-1
    print(c) 
fun([[12,8,5],[4,3,2],[7,5,6]])       
