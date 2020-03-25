def extraLongFactorials(n):
    fac = 1
    if (int(n) >= 1):
        for i in range(1, int(n)+1):
            fac = fac * i
    print(fac)

extraLongFactorials(25)