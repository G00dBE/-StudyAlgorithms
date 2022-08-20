T = int(input())
for t in range(T):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    arr[0][0] = 1                         #초기 원소만 1로 설정
    for i in range(N-1):
        for j in range(i+1):
            if arr[i][j]:                   # 0이 아닌 원소의
                arr[i+1][j] += arr[i][j]    # 바로 아래 원소
                arr[i+1][j+1] += arr[i][j]  #바로 아래의 옆 원소
    print(f"#{t+1}")
    for arr_list in arr:
        for ent in arr_list:
            if ent:
                print(ent, end=" ")
        print()

