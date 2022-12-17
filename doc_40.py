# Q40. Write a function For example, if we give 9119  the function should return  811181, as the  square of 9 is 81 and square of 1  is 1.
def fun(a):
    i=0
    d=str(a)
    while i<len(d):
        print(int(d[i])**2,end="")
        i=i+1        


fun(9119)    