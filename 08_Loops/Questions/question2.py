n=int(input("Enter a number : "))
sum=0;
for i in range(n):
    if i%2==0:
        sum=sum+i

print("Sum of the even numbers till ",n ,"is",sum)