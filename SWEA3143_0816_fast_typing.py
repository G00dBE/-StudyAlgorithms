# SWEA 3143
# 테케에 나오지 않은 반례주의
# babab bab를 생각해보자
T = int(input())
for t in range(1,T+1):
    A, B = input().split()   # A:문자열 입력, B:빠른 타이핑을 위한 문자열
    A_len = len(A)           # A 문자열 길이
    B_len = len(B)           # B 문자열 길이
    cnt = 0                  # 타이핑 수
    start = 0                # 입력 시작점
    while start<A_len:       # A의 인덱스를 넘어가면 종료
        cnt += 1
        if A[start:start+B_len] == B:
            start = start+B_len  # B문자열을 사용하면 입력 시작점을 뒤로
        else:
            start += 1          # B문자열을 사용하지 않으면 시작점 +1
    print(f"#{t} {cnt}")


