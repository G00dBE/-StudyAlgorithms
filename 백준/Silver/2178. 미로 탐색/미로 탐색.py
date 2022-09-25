def bfs(i, j, N, M):
    q = []
    cnt = 0
    arr[i][j] = 0
    cnt += 1
    q.append((i, j, cnt))
    while q:
        a, b, k = q.pop(0)
        if a == N and b == M:
            return k

        else:
            for di, dj in ((-1,0), (0, 1), (1, 0), (0, -1)):
                ni = a + di
                nj = b + dj
                tmp = k
                if 0 <= ni <= N and 0 <= nj <= M:
                    if arr[ni][nj]:
                        arr[ni][nj] = 0
                        tmp += 1
                        q.append((ni, nj, tmp))




N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

print(bfs(0,0, N-1, M-1))
