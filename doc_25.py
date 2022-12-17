# Q25. Given a list of numbers, write a Python program to count positive and negative numbers in a List using function.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3
def sum(a):
    i=0
    p=0
    n=0
    while i<len(a):
        if a[i]>0:
            p=p+1
        else:
            n=n+1
        i=i+1
    print("positive",p,"negetive",n)
sum([2, -7, 5, -64, -14])                

