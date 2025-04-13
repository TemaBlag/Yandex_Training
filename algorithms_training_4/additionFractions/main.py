def nod(a, b):
    delim = max(a, b)
    delit = a + b - delim
    while (delim % delit):
        delim, delit = delit, delim % delit
    return delit


a, b, c, d = map(int, input().split())
delim = nod(a * d + b * c, b * d)
print((a * d + b * c) // delim, b * d // delim)