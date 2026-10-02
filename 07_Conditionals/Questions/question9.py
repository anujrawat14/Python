year = int(input("Enter year :"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year =True
else:
    leap_year = False

print("the enter year ","is" if leap_year==True  else "Not","a leap year")
