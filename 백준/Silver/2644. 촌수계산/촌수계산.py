def bfs(v, w):
    q = []
    visited[v] = 1
    q.append((v, 0))
    while q:
        v1, k1 = q.pop(0)
        for ent in adj[v1]:
            if visited[ent] == 0:
                visited[ent] = 1
                tmp = k1
                if ent == w:
                    return tmp+1

                else:
                    tmp += 1
                    q.append((ent, tmp))

N = int(input())

a, b = map(int, input().split())

m = int(input())

adj = [[] for _ in range(N+1)]

visited = [0]*(N+1)

for i in range(m):
    c, d = map(int, input().split())
    adj[c].append(d)
    adj[d].append(c)


ans = bfs(a, b)
if ans != None:
    print(ans)
elif ans == None:
    print(-1)