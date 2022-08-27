#SWEA1220
#주어진 문제는 1,2 형태의 교착상태만 세면 된다.
for tc in range(1,11):
    N = int(input())  # 크기 입력
    arr = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    for j in range(N):
        for i in range(N):     #세로방향으로 모두 탐색한 후 다음 열로 넘어감
            if arr[i][j] == 1:  # 1인 경우
                arr[i][j] = 0   # 중복으로 세지는 경우 빼기 위해 0으로 만듦
                for k in range(i+1,N):  # 해당좌표의 아래부분만 세면 됨.
                    if arr[k][j] == 2:   # 2인 경우는 교착상태를 세주고 break
                        cnt += 1
                        break
                    elif arr[k][j] == 1:  # 1이 겹쳐져서 나오는 경우는 세지 않고 break
                        break
    print(f"#{tc} {cnt}")