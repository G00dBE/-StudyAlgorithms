def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:  # 출발점을 찾고
                return i, j

def f(i, j, N):          # 도착 여부를 확인 하는 재귀함수, 중복 방문 불필요
    if maze[i][j] == 3:  # 도착
        return 1
    else:
        t_visited[i][j] = False  #방문한 곳 재방문 금지(벽으로 바꿈)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1,0]]:
            ni, nj = i + di , j + dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and t_visited[ni][nj]:
                if f(ni, nj, N):
                    return  1   # 진행방향에서 도착지를 찾은 경우
        return  0           # 도착지 찾지 못하고 리턴

def cnt(i, j, N):          # 거리(칸)을 카운트 하는 함수
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    move = 0
    cnt = 0
    ni = i
    nj = j
    visited[ni][nj] = False
    while True:   # 도착하기 전까지 칸수를 셈
        ni += di[move]
        nj += dj[move]
        if 0<=ni<N and 0<=nj<N and maze[ni][nj] == 1: # 1일 경우 실행 취소
            ni -= di[move]
            nj -= dj[move]
            move = (move+1)%4  # 방향 전환
        elif 0<=ni<N and 0<=nj<N and maze[ni][nj] == 2:  # 출발점으로 돌아왔으므로 cnt 초기화
            cnt = 0
        elif 0<=ni<N and 0<=nj<N and maze[ni][nj] == 0:
            if visited[ni][nj]:
                visited[ni][nj] = False   # 방문한 지점 표시
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
    visited = [[True]*N for _ in range(N)]
    t_visited = [[True] * N for _ in range(N)]
    # 시작점 찾기
    sti, stj = find_start(N)
    if f(sti, stj, N) == 1:
        print(f"#{t+1} {cnt(sti, stj, N)}")
    else:
        print(f"#{t+1} {0}")
