import random

maxxrange = int(input("max range: "))
number = int(input("your number: "))
minn = 0
maxx = maxxrange
n = -1
test = 0
while n != number:
    n = random.randint(minn,maxx)
    if n == number:
        print("your number is", n, "\ntest done: ", test)
    elif number>n:
        test += 1
        print("mine is", n)
        minn = n
    elif number<n:
        test += 1
        print("mine is", n)
        maxx = n
        continue
input()
