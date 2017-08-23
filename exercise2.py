number = input("What is the number:")
if number%4 == 0:
    print("It is a multiple of 4")
elif number%2 == 0:
    print("It is even!")
else: 
    print("It is odd!")
check = input("give a number to check:")
if number%check == 0:
    print("It is a multiple of " + str(check))
else: 
    print("It is not a multiple of " + str(check))
