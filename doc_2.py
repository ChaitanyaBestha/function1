# Write a Python function to find the Max of three numbers.
def max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c 
print(max(40,20,30))            
