import random

a = random.sample(range(0, 50), random.randint(0, 50))

print(a)

def listEnds(a):
    if len(a) <= 2:
        print(a)
    else:
        print([a[0], a[-1]])

listEnds(a)

