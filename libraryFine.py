def libraryFine(d1, m1, y1, d2, m2, y2):
    if (y1 > y2):
        return 10000 * (y1 - y2)
    if (m1 > m2 and y1 == y2):
        return 500 * (m1 - m2)
    if (d1 > d2 and m1 == m2 and y1 == y2):
        return 15 * (d1 - d2)
    if ((d1 == d2 and m1 == m2 and y1 == y2) or y1 < y2 or (m1 < m2 and y1 == y2) or (d1 < d2 and m1 == m2 and y1 == y2)):
        return 0


print(libraryFine(3, 6, 2015, 6, 6, 2015))