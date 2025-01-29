import queue
with open('/Users/user/Documents/input.txt', 'r') as inputFile, open('/Users/user/Documents/output.txt', 'w') as outputFile:
    n, m = list(map(int, inputFile.readline().strip().split()))
    matrix = dict()
    visited = [False] * (n + 1)
    visited[0] = True
    values = [float('inf')] * (n + 1)
    values[0], values[1] = 0, 0
    q = queue.PriorityQueue()
    for i in range(m):
        x, y, value = list(map(int, inputFile.readline().strip().split()))
        matrix.setdefault(x, []).append([y, value])
        matrix.setdefault(y, []).append([x, value])
    v = 1
    q.put((values[v], v))
    while not q.empty():
        v = q.get()[1]
        visited[v] = True
        for u, val in matrix.get(v, []):
            if not visited[u]:
                w = values[v] + val
                if w < values[u]:
                    values[u] = w
                    q.put((values[u], u))
    outputFile.write(str(values[-1]))





