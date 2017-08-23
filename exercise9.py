import random


num = random.randint(1,9)
count = 0

while True:
    guess = input("What is your guess? (0-9): ")

    if guess == "exit":
        break

    guess = int(guess)
    count += 1    
    
    if guess > num:
        print("it is too high!")
    elif guess < num:
        print("it is too low!")
    else:
        print("it is correct. It took you " + str(count) + " tries!")
        count = 0

         
