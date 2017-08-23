
def fib(num):
    count = 2
    fib = []

    if num >= 0:
        fib.append(1)
    if num >= 1:
        fib.append(1)
    while count < num:
        fib.append(fib[count-2] + fib[count-1])
        count += 1
    return fib


a = fib(int(input("How many fibonnaci numbers do you want to generate: ")))
print(a)
