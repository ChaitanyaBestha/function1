# Q41. Write a Python program to find the list with maximum and minimum length.
# Original list:[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])
def fun(a):
    i=0
    max=a[i]
    min=a[i]
    while i<len(a):
        if a[i]>max:
            max=a[i]
        if a[i]<min:
            min=a[i] 
        i=i+1
    print((len(max),max))
    print((len(min),min)) 
fun([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])            