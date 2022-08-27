#SWEA5431
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N: 수강생 수, K: 과제 제출한 사람 수
    check_list = list(map(int, input().split())) # 과제제출자 리스트
    people = [0]*(N+1)    # 전체 명부
    for ent in check_list:  # 숙제 낸 사람 1로
        people[ent] = 1
    print(f"#{tc}", end=" ")
    for i in range(1,N+1):   # 안낸 사람만 출력
        if people[i] == 0:
            print(i, end=" ")
    print()
