def FindPrimeFactors():
    num = 600851475143
    counter = 2;
    primeFactors = [];
    while num > 1:
        if num % counter == 0:
            primeFactors.append(counter)
            num = num / counter
            counter = 2
        counter = counter + 1
    print(max(primeFactors))

FindPrimeFactors()

