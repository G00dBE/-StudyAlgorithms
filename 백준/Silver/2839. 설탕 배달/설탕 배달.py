N = int(input())

a = N//5
b = N%5

ans = []

if b%3 == 0:
    ans.append(a+(b//3))

for i in range(a-1,-1,-1):
    c = N-5*i
    if c%3 == 0:
        ans.append((c//3 + i))

if len(ans) == 0:
    ans.append(-1)

print(min(ans))