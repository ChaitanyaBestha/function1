# Q1.Write a Python program to count the number of strings where the string length is 2     or more and the first and last characters are the same from a given list of strings.
#  ist=['abc', 'xyz', 'aba', '1221']
# result= 2.

def list(a):
    i=0
    while i<len(a):
        d=a[i]
        c=0
        j=0
        while j<len(d):
            if d[j]==d[-1]:
                c=c+1
            j=j+1    
        i=i+1
    print(c)
list(['abc', 'xyz', 'aba', '1221'])            