def recursion(N,i):
    print(n,"X",i,"=",N*i)
    if i<10:
        recursion(N,i+1)
n=int(input("enter the number:"))
recursion(n,1)