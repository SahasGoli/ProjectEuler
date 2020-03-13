def Proj1():
    sum = 0
    for k in range(1000):
        if k % 3 == 0 or k % 5 == 0:
            sum += k
    return sum



print(Proj1())
