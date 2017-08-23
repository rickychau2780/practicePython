import random

upper = int(input("What is the sample upper bound: "))
size = int(input("What is the sample size: "))
number = int(input("What is the greatest number you want to keep from the list: "))
a = random.sample(range(0, 100), 50)
print(a)
print([x for x in a if x <= number])

