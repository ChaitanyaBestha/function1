# Q10.Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):

# "4",  "5" --> "9"
# "34", "5" --> "39"
# Notes:
def fun(a,b):
    c=int(a)
    d=int(b)
    e=c+d
    # f=str(e)
    print('"'+str(e)+'"')
fun('4','5')    