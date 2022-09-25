def dfs(v):
    visited[v] = 1
    for w in adj[v]:
        if visited[w] == 0:
            visited[w] = 1
            dfs(w)


N = int(input())
M = int(input())

adj = [[]*(N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [0]*(N+1)
dfs(1)
cnt = -1
for i in visited:
    if i:
        cnt += 1

print(cnt)
