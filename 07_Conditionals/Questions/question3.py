score=int(input("Enter a  score : "))

if(score>100):
    print("please verify your score")
    exit()

if(score<60):
    print("You got grade : F")
elif(score<70):
    print("You got grade : D")
elif(score<80):
    print("You got grade : C")
elif(score<90):
    print("You got grade : B")
else:
    print("You got grade : A")
