# SWEA 1979
# 2차원 배열 문제
T = int(input())
for t in range(T):
    N, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    trans_arr = list(zip(*arr))
    cnt = 0
    word_list = [1] * m
    for i in range(N):
        if arr[i][0:m+1] == word_list+[0]:
            cnt += 1
        if arr[i][-1:-m-2:-1] == word_list+[0]:
            cnt += 1
        if list(trans_arr[i][0:m+1]) == word_list+[0]:
            cnt +=1
        if list(trans_arr[i][-1:-m-2:-1]) == word_list+[0]:
            cnt += 1
        for j in range(N-m-1):
            if arr[i][j:j+m+2] == [0]+word_list+[0]:
                cnt += 1
            if list(trans_arr[i][j:j+m+2]) == [0]+word_list+[0]:
                cnt += 1
    print(f"#{t+1} {cnt}")