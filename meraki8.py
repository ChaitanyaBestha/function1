# def fun(l1,l2):
# #setting range till the length of l1
# for i in range(len(l1)):
#  sum=l1[i]+l2[i]
#  print(sum)
# #passing two list as an arguments to our function
# list1=[10,20,30]
# list2=[40,50,60]
# fun(list1,list2)

def fun(l1,l2):
    i=0
    c=0
    while i<len(l1):
        c=l1[i]+l2[i]
        # sum=sum+c
        i=i+1
        print(c)
l1=[10,20,30]
l2=[40,50,60] 
fun(l1,l2)   
