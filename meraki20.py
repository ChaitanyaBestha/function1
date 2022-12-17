# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# #Doing sorting of all the elements present in the list using sorted inbuilt function
# print(sorted(unorder_list))
def number(a):
    i=0
    while i<len(a):
        a.sort()
        i=i+1
    print(a) 
number([6, 8, 4, 3, 9, 56, 0, 34, 7, 15])       