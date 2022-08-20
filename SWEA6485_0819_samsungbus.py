# SWEA 6485
T = int(input())
for t in range(T):
    N = int(input()) # 노선 수
    bus_stop = [0] * 5001  # 버스 정류장 전체
    for i in range(N):
        a, b = map(int, input().split())  # 노선번호
        for j in range(a, b+1):
            bus_stop[j] += 1             #지나는 노선 구간에 +1 씩
    P = int(input())
    idx = [bus_stop[int(input())] for _ in range(P)]  # 지나는 버스 정류장 목록
    print(f"#{t+1}", end=" ")
    for ent in idx:
        print(ent, end=" ")
    print()