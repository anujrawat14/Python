# prime number factor na ho 1 and number itself

num = int(input("enter a number : "))
isPrime = True

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break


print("the number u enter is a prime : ",isPrime)