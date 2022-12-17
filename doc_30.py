# Q30. Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
# a=int(input("enter no:"))
# i=1
# while i<=a:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c=c+1
#         j=j+1
#     if c==2:
#         print(i,end=" ")
#     i=i+1            
def fun(a,b):
    i=a
    while i<=b:
        j=1
        c=0
        while j<=i:
            if i%j==0:
                c=c+1
            j=j+1    
        if c==2:
            print(i,end=" ")
        i=i+1    
fun(1,200)        
