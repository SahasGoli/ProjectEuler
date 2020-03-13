def sumOfSquares():
    sumOfSquares = 0
    for k in range(1,101):
        sumOfSquares += k*k
    
    return sumOfSquares

def squareOfSum():
    squareOfSum = sum(range(1,101))
    squareOfSum = squareOfSum * squareOfSum
    return squareOfSum

answer = sumOfSquares() - squareOfSum()
print(answer)