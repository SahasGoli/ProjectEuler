def smallestMultiple():
    num = 20
    notDivisibleByAll = True
    while notDivisibleByAll == True:
        num = num + 20
        notDivisibleByAll = False
        for k in range(1,21):
            if num % k != 0:
                notDivisibleByAll = True

    print(num)


smallestMultiple()