import random


a = random.sample(range(0,50), 20)
b = random.sample(range(0,50), 25)
print(a)
print(b)

print(list(set(a).intersection(set(b))))
