import random

a = random.sample(range(0, 100), 50)
print([x for x in a if x%2 == 0])
