def prefixFunction(string):
    p = [0] * lenString
    for i in range(1, lenString):
        k = p[i-1]
        while k > 0 and string[k] != string[i]:
            k = p[k - 1]
        if string[k] == string[i]:
            p[i] = k + 1
        else:
            p[i] = k
    return p[lenString - 1]


string = input()
lenString = len(string)
print(lenString - prefixFunction(string))