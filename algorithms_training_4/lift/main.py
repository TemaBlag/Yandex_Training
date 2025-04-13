"""
k = int(input())
n = int(input())
people = [int(input()) for floor in range(n)]
countPeople = sum(people)
answer = 0
i = n - 1
while countPeople:
    while people[i] == 0:
        i -= 1
    liftMembers = k
    coef = people[i] // liftMembers
    countPeople -= people[i]
    people[i] = people[i] % liftMembers
    answer += 2*(i+1) * coef
    liftMembers = people[i]
    people[i] = 0
    if people[0] == 0 and liftMembers == 0 and i == 0:
        break
    answer += 2 * (i+1)
    i -= 1
    if i < 0:
        break
    while liftMembers:
        if liftMembers - people[i] >= 0:
            countPeople -= people[i]
            liftMembers -= people[i]
            i -= 1
        else:
            countPeople -= liftMembers
            people[i] -= liftMembers
            liftMembers = 0
            break
print(answer)
"""
k = int(input())
n = int(input())
people = [int(input()) for floor in range(n)]
countPeople = sum(people)
answer = 0
i = n - 1
while countPeople:
    liftMembers = k
    while not people[i]:
        if i - 1 >= 0:
            i -= 1
        else:
            break
    # people[i] != 0
    times = people[i] // liftMembers
    answer += 2*(i+1)*times
    countPeople -= times*liftMembers
    liftMembers -= liftMembers if people[i] % liftMembers == 0 and times else people[i] % liftMembers
    if not liftMembers:
        people[i] = 0
        continue
    countPeople -= k - liftMembers
    people[i] = 0
    answer += 2 * (i + 1)
    if i - 1 >= 0:
        i -= 1
    else:
        break
    # 0 < liftMembers curr < liftMembers start
    while liftMembers >= people[i]:
        liftMembers -= people[i]
        countPeople -= people[i]
        people[i] = 0
        if i - 1 >= 0:
            i -= 1
        else:
            break
    # liftMembers < people[i]
    people[i] -= liftMembers
    countPeople -= liftMembers
    liftMembers = 0
print(answer)



