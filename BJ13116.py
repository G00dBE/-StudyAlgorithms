#주어진 문제는 완전이진 트리의 공통 조상을 찾는 문제

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    lst = []
    ans = 0
    if N > M:
        while M>0:
            lst.append(M)
            M = M//2
        
        while N>0:
            if N in lst:
                ans = N
                break
            else:
                N = N//2 
    elif N == M:
        ans = N
    
    else:
        while N>0:
            lst.append(N)
            N = N//2
        
        while M>0:
            if M in lst:
                ans = M
                break
            else:
                M = M//2 
                
        
                       
    print(ans*10)