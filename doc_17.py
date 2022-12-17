# Q17. Write a function to tell user if he/she is able to vote or not.( Consider minimum age of voting to be 18. )
def vote(name,age=18):
    if age>=18:
        print(name,"is able to vote")
    else:
        print(name,"is not eligible")  
vote("chaitu")          