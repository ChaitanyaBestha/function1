# Q35. Kids drink toddy.
# 	Teens drink coke.
# 	Young adults drink beer.
# 	Adults drink whisky.
# 	Make a function that receive age, and return what they drink.
# Rules:-
# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
# Examples: (Input --> Output)

# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky".
def gen(age):
    if age<14:
        print(age,"kids drink toddy")
    elif 14<=age and age<18:
        print(age,"teens drink coke")
    elif 18<=age and age<21:
        print(age,"youngsters drink beer")
    elif 21<=age and age<30:
        print(age,"adults drink whisky")
    else:
        print("drink whatever they want")
gen(14)            
