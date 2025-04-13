string1, string2 = input(), input()
dct1 = {}
dct2 = {}
k = ""
for le in string1:
    dct1[le] = dct1.get(le, 0) + 1
for le in string2:
    dct2[le] = dct2.get(le, 0) + 1
for key, val in dct1.items():
    if dct2.get(key) != val:
        k = "NO"
        break
print("YES") if k == "" else print(k)