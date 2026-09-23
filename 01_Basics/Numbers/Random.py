import random

random_Number=random.random()

print(random_Number)

# in range
random_Number=random.randint(1,10);
print(random_Number)

#in array

random_Number=random.choice([1,2,3])
print(random_Number)


#shuffle 
l1=[1,2,3,4]
random.shuffle(l1)
print(l1)
