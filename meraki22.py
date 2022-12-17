# list = [8, 6, 4, 8, 4, 50, 2, 7]
# #Using min inbuilt function we are printing minimum value from list
# print(min(list))

def chinna(a):
    i=0
    min=1000
    while i<len(a):
        if a[i]<min:
            min=a[i]
        i=i+1
    print(min) 
chinna([8, 6, 4, 8, 4, 50, 2, 7])           
