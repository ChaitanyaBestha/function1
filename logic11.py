def zero(a):
    i=0
    j=str(a)
    while i<len(j):
        if j[i]!="0":
            print(j[i],end="")
        i+=1
zero([1200,1502,14020,2002])