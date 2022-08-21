# SWEA 1221
# 정렬을 꼭 할 필요는 없다.
T = int(input())
for t in range(T):
    tc, n = input().split()  # 테케 번호/문자열길이
    N = int(n)              # 문자열-> 정수형
    K = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    str_num = list(input().split())  # 문자열 리스트로 입력
    str_num_sorted = []
    for i in range(10):     # 리스트 K를 앞부터 순회
        for j in range(N):  # 입력 리스트에 같은 값이 있으면
            if K[i] == str_num[j]:
                str_num_sorted += [str_num[j]]  # 그 값을 정렬 리스트에 추가
    print(tc)
    print(" ".join(str_num_sorted))