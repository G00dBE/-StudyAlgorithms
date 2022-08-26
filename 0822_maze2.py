def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:  # 출발점을 찾고
                return i, j


def cnt(i, j, N):          # 거리(칸)을 카운트 하는 함수
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    visited = []  # 방문한 점을 저장
    move = 0
    cnt = 0
    ni = i
    nj = j
    while True:   # 도착하기 전까지 칸수를 셈
        visited.append((ni, nj))
        ni += di[move]
        nj += dj[move]
        if 0<=ni<N and 0<=nj<N and maze[ni][nj] == 1: # 1일 경우 실행 취소
            ni -= di[move]
            nj -= dj[move]
            move = (move+1)%4  # 방향 전환
        elif 0<=ni<N and 0<=nj<N and maze[ni][nj] == 2:  # 출발점으로 돌아왔으므로 cnt 초기화
            cnt = 0
        elif 0<=ni<N and 0<=nj<N and maze[ni][nj] == 0:
            if (ni, nj) not in visited:
                cnt += 1
        elif ni<0 or ni>=N or nj<0 or nj>=N:  #인덱스를 벗어난 경우
            ni -= di[move]
            nj -= dj[move]
            move = (move + 1) % 4  # 방향 전환
        elif 0<=ni<N and 0<=nj<N and maze[ni][nj] == 3: # 도착한 경우 루프 종료
            break
    return cnt


T = int(input())
for t in range(T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # 시작점 찾기
    sti, stj = find_start(N)

    print(f"#{t+1} {cnt(sti, stj, N)}")
