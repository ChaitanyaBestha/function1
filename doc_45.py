# Q45. Draw a flowchart to Take 10 numbers as input and create a list of the numbers from the user and update each element of the list according to below rule
# If it is even, then multiply it by 100
# If it is odd, then multiply it by -1 
# Sample Input:
# 	23
# 	42 
# 	41 
# 	1
# Sample Output:
# 	-23 
# 	4200 
# 	-41 
# 	-1

def fun(a):
    i=1
    b=[]
    while i<=a:
        n=int(input("enter no:"))
        b.append(n)
        i=i+1
    print(b) 
    j=0
    c=[]
    while j<len(b):
        if b[j]%2==0:
            c.append(b[j]*100)
        else:
            c.append(b[j]*(-1))
        j=j+1
    print(c)    
fun(4)    