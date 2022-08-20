# SWEA 1979
# 2차원 배열 문제
T = int(input())
for t in range(T):
    N, K = map(int, input().split())   # NxN 행렬 크기, 단어길이
    arr = [list(map(int, input().split())) for _ in range(N)] # 퍼즐 입력
    trans_arr = list(zip(*arr))               # 위아래 탐색 시 필요한 전치 행렬
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j:j+K] == [1]*K:   # 원래 퍼즐에서 단어가 들어갈 공간 탐색
                if (0<=(j-1)<N and arr[i][j-1] == 1) or (0<=(j+K)<N and arr[i][j+K] == 1):
                    pass
                else:
                    cnt += 1
    for i in range(N):
        for j in range(N):
            if trans_arr[i][j:j+K] == (1,)*K:  # 전치 행렬에서 단어가 들어갈 공간 탐색/튜플자료형
                if (0<=(j-1)<N and trans_arr[i][j-1] == 1) or (0<=(j+K)<N and trans_arr[i][j+K] == 1):
                    pass
                else:
                    cnt += 1
    print(f"#{t+1} {cnt}")
