def dfs():
    global cnt
    while len(stack)>0:
        i, j = stack.pop()
        for di, dj in ((-1,0), (0,1), (1,0), (0,-1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < M and 0 <= nj <N:
                if arr[ni][nj] == 0:
                    cnt += 1
                    arr[ni][nj] = 1
                    stack.append((ni, nj))

M, N, K = map(int, input().split())
arr = [[0]*N for _ in range(M)]

stack = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(M-y1-1, M-y2-1,-1):
        for j in range(x1, x2):
            arr[i][j] += 1

cnt = 0
ans = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            arr[i][j] = 1
            cnt += 1
            stack.append((i, j))
            dfs()

        if cnt != 0:
            ans.append(cnt)
            cnt = 0
ans.sort()
print(len(ans))
for ent in ans:
    print(ent, end=" ")