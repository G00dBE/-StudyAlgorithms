#swea4466
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    sum_all = 0
    score.sort(reverse=True)
    for i in range(K):
        sum_all += score[i]
    print(f"#{t} {sum_all}")
