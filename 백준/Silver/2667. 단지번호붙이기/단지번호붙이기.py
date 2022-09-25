def dfs(i,j):
    global cnt
    while len(stack):
        a, b = stack.pop()
        for di, dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni = a + di
            nj = b + dj
            if 0 <= ni < N and 0 <= nj <N:
                if arr[ni][nj]:
                    cnt += 1
                    arr[ni][nj] = 0
                    stack.append((ni, nj))

N = int(input())
arr = [list(map(int,input())) for _ in range(N)]

stack = []

ans = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt = 1
            arr[i][j] = 0
            stack.append((i, j))
            dfs(i, j)
            ans.append(cnt)

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])

