

def dfs(v):
    visited[v] = 1
    stack.append(v)
    print(v, end=" ")
    if stack:
        u = stack.pop()
        for w in adj[u]:
            if visited[w] == 0:
                dfs(w)


def bfs(v):
    q = []
    q.append(v)
    bvisited = [0]*(N+1)
    
    while q:
        w = q.pop(0)
        print(w, end=" ")
        bvisited[w] = 1                

        
        for u in adj[w]:
            if bvisited[u] == 0:
                bvisited[u] = 1
                q.append(u)
                
N, M, V = map(int, input().split())

adj = [[]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for ent in adj:
    ent.sort()

stack = []
visited = [0]*(N+1) 

dfs(V)
print()
bfs(V)
print()
