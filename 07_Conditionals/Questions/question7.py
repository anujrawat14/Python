order=input("Enter ur coffee size : ").lower();

extra_shot=input("want extra shot (yes/No) : ").lower();

extra_shot_added="yes" if extra_shot=="yes" else "no";

if(order=="small"):
    bill="Small"
elif(order=="medium"):
    bill="Medium"
else:
   bill="Large"


print("U order",bill, " size coffee with",extra_shot_added," extra shot of espresso")