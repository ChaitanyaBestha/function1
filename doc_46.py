# Q46. Draw a flowchart to take a list of N numbers from the user, print True if the complete list consists of consecutive numbers with a difference of one. Print False otherwise. 

# Sample Input:
# 1 2 3 4 5 6 7
# Sample Output:
# True
# Sample Input:
# 45 46 47 48 49 51 52
# Sample Output:
# False
def fun(a):
    i=0
    v=a[1]-a[0]
    result=True
    while i<len(a)-1:
        r=a[i+1]-a[i]
        if v==r:
            result=True
        else:
            result=False
            break
        i=i+1
    return result
print(fun([45,46,47,48,49,51,52]))    