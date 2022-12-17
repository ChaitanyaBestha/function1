# Q12.Numbers ending with zeros are boring.

# They might be fun in your world, but not here.

# Get rid of them. Only the ending ones.

# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
def fun(a):
    i=0
    b=[]
    while i<len(a):
        j=0
        k=a[i]
        while j<k:
            if k%10==0:
                k=k//10
            j=j+1
        b.append(k)
        i=i+1
    print(b)
fun([1450,960000,1050,-1050])            
