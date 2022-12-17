# Q44.Bonus - Given the same list, print the last ‘N’ elements in reverse order.
# Sample Input:
# 2
# Sample Output:
# q
# b 
# Sample Input:
# 3
# Sample Output:
# q
# b 
# 5
def fun(a):
    # i=0
    # b=[]
    # while i<a:
    #     n=int(input("enter"))
    #     b.append(n)
        # i=i+1
    # print(b)
    n=int(input("enter:"))
    j=-1
    while j>=-(len(a)-n):
        print(a[j])
        j=j-1    
fun(['a', 1, '2', 5, 'b', 'q'])    