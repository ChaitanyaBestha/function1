# Q9.Write a Python program to generate and print a list of first and last 5 elements where 
#   the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).

def fun(a,b):
    i=0
    f=[]
    c=[]
    while i<len(a):
        d=a[i]*a[i]
        f.append(d)
        e=b[i]*b[i]
        c.append(e)
        i=i+1
    print(f,c)
fun([1,2,3,4,5],[26,27,28,29,30])        