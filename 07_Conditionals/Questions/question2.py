# age=10;
age = int(input("enter your  age : "))
day = input("enter day : ")
ticket_adult = 12
ticket_child = 8

# using nested loops

# if age >= 18:
#     if day == "Wednesday":
#         ticket_adult -= 2;
#     print("price of ticket is $", ticket_adult);

# else:
#      if day == "Wednesday":
#         ticket_child -=2;
#      print("price of ticket is $", ticket_child);

# using simple loops

# if day == "Wednesday":
#         ticket_child -= 2
#         ticket_adult-=2

# if age >= 18:
#     print("price of ticket is $", ticket_adult);

# else:
#      print("price of ticket is $", ticket_child);


#giving price base on age

price=12 if age>=18 else 8;

if day=="Wednesday":
    price=price-2;

print("price of ticket is $",price)