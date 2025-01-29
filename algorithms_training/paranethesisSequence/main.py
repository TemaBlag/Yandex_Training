string = input()
brackets = []
dct = {"{": "}", "(": ")", "[": "]"}
answer = True
for el in string:
    if el in ["(", "{", "["]:
        brackets.append(el)
    else:
        if len(brackets) == 0 or el != dct[brackets[-1]]:
            answer = False
        else:
            brackets.pop()
print("yes") if answer and len(brackets) == 0 else print("no")