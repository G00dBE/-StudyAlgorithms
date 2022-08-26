#최댓값은 (N을 P로 나눈 몫) + (N을 P로 나눈 나머지가 있을 경우 나머지 만큼 각 몫에 +1)
T = int(input())
for t in range(1, T+1):
    N, P = map(int, input().split())   # N : 달란트 , P : 묶음의 수
    Q = N//P                           # 몫
    R = N%P                            # 나머지
    ans = (Q**(P-R))*((Q+1)**R)
    print(f"#{t} {ans}")