password=input("Enter your password : ")
length=len(password);

if length<6:
    strength="Weak"
elif length<10:
    strength="Medium"
else:
    strength="Strong"

print("Ypur password strength is ",strength)