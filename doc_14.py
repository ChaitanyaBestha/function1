# Q14.Write a function to check if a number is prime or not.

def num(a):
    i=1
    c=0
    while i<=a:
        if a%i==0:
            c=c+1
        i=i+1
    if c==2:
        print("prime")
    else:
        print("not prime")
num(17)                    
