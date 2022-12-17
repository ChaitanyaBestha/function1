# Q43.  Make a function given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’]. Print the last ‘N’ elements of the given list. ‘N’ is accepted from the user.
# Sample Input:
# 1
# Sample Output:
# q 
# Sample Input:
# 3
# Sample Output:
# 5
# b 
# q

def fun(a):
    n=int(input("enter no:"))
    i=len(a)-n
    while i<len(a):
        print(a[i])
        i=i+1
fun(['a', 1, '2', 5, 'b', 'q'])    
