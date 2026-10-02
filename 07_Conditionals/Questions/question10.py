pet=input("Enter your pet species : ").lower()
age=int(input("ENter age of ur pet : "))

if pet=="dog":
    if age<2:
        print("give puppy food to your dog")
    else:
        print("No information")

elif pet=="cat":
     if age>2:
            print("Senior Cat Food to your cat")
     else:
            print("No information ")
    
else:
     print("the pet u enter have no diet plans ")