items = ["apple", "banana", "orange", "apple", "mango"]

# method 1

# items=input("Enter a list : ").split()
# for char in items:
#     if(items.count(char)>1):
#         print(char ," is duplicate")
#         break


#  method 2 
unique_item=set()

for char in items:
    if char in unique_item:
        print(char , " is duplicate ")
        break
    unique_item.add(char)