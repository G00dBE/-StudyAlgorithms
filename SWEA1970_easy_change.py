#SWEA1970
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    change_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10] # 거스름돈 리스트
    use = [0,0,0,0,0,0,0,0]
    for i in range(8):
        if change_list[i] <= N: # 거스름돈이 N보다 작으면
            use[i] = N//change_list[i]  #몫을 사용리스트에 저장하고
            N = N%change_list[i]        # N에 나머지를 저장
    print(f"#{tc}")
    for i in range(8):
        print(use[i], end=" ")
    print()