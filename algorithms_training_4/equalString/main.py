def equalStrings(length, a, b):
    return "yes" if (h[a + length] + h[b] * xDeg[length]) % p\
                    == (h[b + length] + h[a] * xDeg[length]) % p else "no"


string = input()
lenString = len(string)
x = 10
p = 10 ** 9 + 7
xDeg = [0] * (lenString + 1)
xDeg[0] = 1
h = [0] * (lenString + 1)
string = " " + string
for i in range(1, lenString + 1):
    h[i] = ((h[i-1] * x) + ord(string[i])) % p
    xDeg[i] = (xDeg[i-1] * x) % p
answers = []
for _ in range(int(input())):
    answers.append(equalStrings(*map(int, input().split())))
print(*answers, sep="\n")

