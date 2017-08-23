num = int(input("Please give a number: "))
if num < 2:
    print(num)
else:
    print([x for x in range(2, num/2+1) if num%x ==0])
