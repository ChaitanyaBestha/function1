def fib(a):
    if a<=1:
        return a
    else:
        return (fib(a-1)+fib(a-2))
n=int(input("enter no:"))
if n>0:
    i=0
    while i<=n:
        print(fib(i))
        i=i+1