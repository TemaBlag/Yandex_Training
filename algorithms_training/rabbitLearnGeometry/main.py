"""
#overkill
n, m = map(int, input().split())
matrix = []
answer = 0
for x in range(n):
    matrix.append(list(map(int, input().split())))
for x in range(n):
    if x + answer >= n:
        break
    for y in range(m):
        if y + answer >= m:
            break
        k = 0
        if matrix[x][y]:
            k += 1
            flag = True
            while x + k < n and y + k < m and flag:
                if matrix[x+k][y+k] == 0:
                    answer = k if answer < k else answer
                    flag = False
                    break
                for dif in range(k):
                    if matrix[x + dif][y + k] == 0 or matrix[x + k][y + dif] == 0:
                        answer = k if answer < k else answer
                        flag = False
                        break
                k += 1
            if flag:
                answer = k if answer < k else answer
print(answer)
"""
n, m = map(int, input().split())
matrix = []
sums = [[0]*(m+1) for _ in range(n+1)]
answer = 0
for x in range(n):
    matrix.append(list(map(int, input().split())))
for x in range(n):
    for y in range(m):
        if matrix[x][y]:
            sums[x+1][y+1] = min(sums[x][y], sums[x][y+1], sums[x+1][y]) + 1
            if sums[x+1][y+1] > answer:
                answer = sums[x+1][y+1]
print(answer)