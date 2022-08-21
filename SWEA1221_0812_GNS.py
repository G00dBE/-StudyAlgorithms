# SWEA 1221
# 카운팅 정렬 O(n+k) 을 연습해보기 좋은 예제
# K = 10
T = int(input())
for t in range(T):
    tc, n = input().split()  # 테케 번호/문자열길이
    N = int(n)              # 문자열-> 정수형
    K = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    str_num = list(input().split())  # 문자열 리스트로 입력
    cnt = [0]*10                     # count할 리스트 생성
    sort_str_num = [0]*N             # 정렬된 원소를 담을 리스트
    for i in range(N):    # 입력받은 리스트 원소와 값이 일치하는 num의 인덱스
        cnt[K.index(str_num[i])] += 1 # cnt에 각각 인덱스에 따른 개수를 누적
    for i in range(9):
        cnt[i+1] += cnt[i]       # 이전 인덱스 값을 뒤 인덱스에 누적
    for i in range(N-1,-1,-1):   # 뒤쪽 부터
        cnt[K.index(str_num[i])] -= 1  # 입력 받은 리스트의 맨뒤의 값에 해당하는 K리스트의 인덱스/cnt감소하고
        sort_str_num[cnt[K.index(str_num[i])]] = str_num[i] # 카운트 인덱스에 입력 리스트의 값을 정렬
    print(tc)
    print(" ".join(sort_str_num))