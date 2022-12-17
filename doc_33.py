# Q33. Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi > 30 return "Obese"
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"

def bmi(weight,height):
    bmi=(weight/(height*height))
    if bmi<=18.5:
        c="underweight"
        return c
    elif bmi<=25.0:
        c="normal"
        return c
    elif bmi<=30.0:
        c= "overweight" 
        return c
    elif bmi>30:
        c="obese"
        return c
weight=(int(input("enter no:")))
height=(int(input("enter no:")))        
print(bmi(weight,height))           