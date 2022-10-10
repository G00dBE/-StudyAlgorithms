N = int(input())
lst = tuple(map(int, input().split()))

cnt = 0

for i in range(N):
    if lst[i] != 1 and lst[i]%2 != 0:
        for j in range(2, lst[i]):
            if lst[i]%j == 0:
                break
        else:
            cnt += 1
    elif lst[i] == 2:
        cnt += 1

print(cnt) 