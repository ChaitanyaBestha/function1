# Write a function which converts the input string to uppercase.
# For example:-
# [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
# Input sequence contains minimum two elements and every element is an integer.
def man(a):
    i=0
    max1=0
    max2=0
    while i<len(a):
        if a[i]>max1:
            max1=a[i]
        elif a[i]>max2 and max2!=max1:
            max2=a[i]
        c=max1+max2
        i=i+1
    print(c)
man([99, 2, 2, 23, 19])                
