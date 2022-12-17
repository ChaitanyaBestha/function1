# reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# #Using reverse function we are doing reversing of our list
# reverse_list.reverse()
# print(reverse_list)
def reverse(a):
    i=-1
    b=[]
    while i>=-len(a):
        b.append(a[i])
        i=i-1
    print(b)
reverse(["Z", "A", "A", "B", "E", "M", "A", "R", "D"])        