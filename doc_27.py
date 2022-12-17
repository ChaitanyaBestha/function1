# Q27. Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”
def fun (a):
    if a<=70:
        print("ok")
    elif a>=70 and a<=130:
        b=(a-70)//5
        print("points:",b)
        if b>=12:
            print("license suspended")
        else:
            print("better luck next time")    
            
    else:
        print("enter valid data")            
fun(int(input("enter")))    