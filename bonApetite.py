import math

def bonAppetit(bill, k, b):
    bill.pop(k)
    half = math.floor(sum(bill)/2)
    if (half == b):
        print('Bon Apetite')
    else:
        print(b - half)
bonAppetit([3, 10, 2, 9], 1, 12)