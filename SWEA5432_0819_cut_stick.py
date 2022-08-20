# SWEA 5435
T = int(input())
for t in range(1, T+1):
    stick = input()      # 문자열 형태로 입력받음
    cnt = 1              # 막대기 하나를 자르면 두조각/값을 1로 초기화
    end = 0
    pieces = 0
    for i in range(1,len(stick)):
        if stick[i] == "(":   # ( 은 막대기의 시작이므로 1증가
            cnt += 1
        elif stick[i] == ")":   # ) 은 막대기의 끝이므로 1 감소
            cnt -= 1
            if stick[i-1] == "(":  # () 레이저/cnt를 저장
                pieces += cnt
            else:
                end += 1        # 막대기 끝/ 자르고 남은 조각 한개 더함
    print(f"#{t} {pieces+end}")
