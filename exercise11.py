num = int(input("What is the number you want to check: "))

def checkPrime(num):
    divisors = [x for x in range(2, int(num/2)+1) if num%x == 0]
    if divisors:
        print("It is not a prime!")
    else:
        print("It is a prime!")

checkPrime(num)

