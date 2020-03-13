def fib():
    n1 = 0;
    n2 = 1;
    sum = 0;
    while n2 < 4000000:
        ntemp = n1+n2
        n1 = n2
        n2 = ntemp
        if ntemp % 2 == 0:
            sum += ntemp
    return sum


print(fib())



