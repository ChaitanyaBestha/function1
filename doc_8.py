# Q8.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12

def fun(a):
    i=0
    while i<len(a):
        j=0
        cu=0
        cl=0
        while j<len(a[i]):
            if a[i][j].isupper()==True:
                cu=cu+1
            else:
                cl=cl+1
            j=j+1
        i=i+1
    print("no of upper",cu)
    print("no of lower",cl)
fun(['The quick Brow Fox'])                    
