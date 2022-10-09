N, K = map(int, input().split())

ans = 0

visited = [0]*100001

front = 0

if N==K:
    pass
else:
    q = []
    
    if 100000>=N+1>=0:
        q.append((N+1,1))
        visited[N+1] = 1
        
    if 100000>=N-1>=0:
        q.append((N-1,1))
        visited[N-1] = 1
    
    if 100000>=N*2>=0:
        q.append((N*2,1))
        visited[N*2] = 1
    
    while q:
        a,t = q[front]
        
        if a == K:
            ans = t
            break
        
        else:
            if 100000>=a+1>=0 and visited[a+1] == 0:
                q.append((a+1,t+1))
                visited[a+1] = 1
            
            if 100000>=a-1>=0 and visited[a-1] == 0:
                q.append((a-1,t+1))
                visited[a-1] = 1
        
            if 100000>=a*2>=0 and visited[a*2] == 0:
                q.append((a*2,t+1))
                visited[a*2] = 1    
            
            front += 1

print(ans)
