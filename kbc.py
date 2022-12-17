def fun():
    questions=["which is the third highest civilian in india","Name the river bank on which tajmahal is situated",
            "What is the national song of india","which was the first satellite of india"]
    options=[["1.bharat ratna","2.padma bhusan","3.padma sri","4.padma vibhushan"],
        ["1.ganges","2.yamuna","3.godavari","4.indus"],
        ["1.vande matharam","2.gana gana mana","3.sare jaha se accha","4.mera desh ki darti"],
        ["1.bhaskara","2.aryabhata","3.rohini","4.kalpana"]]
    solutions=[1,2,2,2] 
    solution=0 
    i=0
    while i<len(options):
        print(questions[i])
        j=0
        while j<len(options[i]):
            print(options[i][j])
            j=j+1
        answer=int(input("enter your answer"))
        if answer==solutions[solution]:
            print("your answer is correct")
        else:
            print("oops! ,your answer is wrong")
            print("quit")
            break
        solution=solution+1    
        i=i+1
print("welcome to kbc") 
a=(input("enter name:"))
fun()  
    

