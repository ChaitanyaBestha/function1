a=[12300,1620,150,20,74820]
i=0
b=[]
while i<len(a):
    k=a[i]
    j=0
    while j<k:
        if k%10==0:
            k=k//10
        j=j+1
    b.append(k)
    i=i+1
print(b)
