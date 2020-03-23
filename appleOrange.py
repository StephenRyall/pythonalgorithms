def countApplesAndOranges(s, t, a, b, apples, oranges):
    totApp = 0
    totOran = 0
    for i, app in enumerate(apples):
        apples[i] = app + a
        if (s <= apples[i] and t >= apples[i]):
            totApp += 1
    for j, oran in enumerate(oranges):
        oranges[j] = oran + b
        if (s <= oranges[j] and t >= oranges[j]):
            totOran += 1
    print([totApp, totOran])

countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])