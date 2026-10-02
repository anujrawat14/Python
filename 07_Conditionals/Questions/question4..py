fruit=input("Enter fruit : ")
color=input("Enter colour of fruit : ")

if(fruit=="Banana"):
    if(color=="green"):
         print("Unripe ")
    elif(color=="yellow"):
        print(" Ripe ")
    else:
        print(" Overripe ")
else :
    print("no data available for this ",fruit)
    exit()