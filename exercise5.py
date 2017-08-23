import random

a = random.sample(range(0, 50), 20)
b = random.sample(range(0, 50), 15)
print(a)
print(b)
#c = [x for x in a if x in b and x not in c]
c = list(set(a).intersection(set(b)))
print(c)

