# Q4.Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Output : "dcba4321".
def sunny(a):
    i=0
    while i<len(a):
        c=""
        j=-1
        while j>=-len(a[i]):
            c=c+a[i][j]
            j=j-1
        i=i+1
    print('"'+c+'"')        
    
sunny(["1234abcd"])        