#SWEA6019
T = int(input())
for t in range(1,T+1):
    D, A, B, F = map(int, input().split()) # D: 두 기차 전면부 사이 거리, A: A기차 속력, B: B기차 속력, F: 파리의 속력
    time = D/(A+B)      # 시간 = (두 기차 사이 거리)/(두 기차의 속력의 합)
    print(f"#{t} {F*time}")