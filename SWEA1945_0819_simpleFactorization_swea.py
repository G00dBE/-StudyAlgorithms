# SWEA 1945
# 소인수는 2, 3, 5, 7, 11로 한정
T = int(input())              # 테스트 케이스 입력
for t in range(T):
    N = int(input())          # 소인수분해할 수 입력
    prime = [2, 3, 5, 7, 11]  # 소인수 목록
    cnt = [0]*5               # 소수로 나누어 떨어진 횟수 저장
    for i in range(5):
        while N%prime[i] == 0:# 각 소인수로 나누어 떨어지지 않을 때까지 여러번 나눔
            cnt[i] += 1
            N = N//prime[i]
    print(f"#{t+1}", end=" ")
    for ent in cnt:
        print(ent, end=" ")
    print()
