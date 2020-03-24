import math

def squares(a, b):
    sqrtA = math.ceil(math.sqrt(a))
    sqrtB = math.floor(math.sqrt(b))
    return(sqrtB - sqrtA + 1)

print(squares(20, 55))