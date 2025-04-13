import math
pi = math.pi
x1, y1, x2, y2 = map(int, input().split())
r1 = (x1**2 + y1**2)**0.5
r2 = (x2**2 + y2**2)**0.5
dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
alpha1 = math.atan2(y1, x1)
alpha2 = math.atan2(y2, x2)
alpha = abs(2 * pi - (abs(alpha1 - alpha2))) if (abs(alpha1 - alpha2)) > pi else (abs(alpha1 - alpha2))
r = r1 + r2
s = min(r1, r2) * alpha + max(r1, r2) - min(r1, r2)
print(min(s, r))




