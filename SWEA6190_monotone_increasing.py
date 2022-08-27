#swea6190
T = int(input())
for t in range(1,T+1):
    N = int(input())
    num = list(map(int, input().split()))
    num_list = []
    for i in range(N):
        for j in range(N):
            if i != j:                      # 같은 수끼리 곱해져서 단조증가되는 경우 제외
                num_list.append(num[i]*num[j])
    mono = []   # 단조 증가하는 수를 담을 리스트
    for ent in num_list:
        mono.append(ent)
        while ent:
            r = ent%10     # 나머지와
            ent = ent//10  # 몫의 크기를 비교
            ent0 = ent%10
            if ent0 > r:
                mono.pop()
                break
    if len(mono):   # 공집합이 아닌 경우만 실행
        max_ent = mono[0]
        for ent in mono:
            if max_ent < ent:
                max_ent = ent
        print(f"#{t} {max_ent}")
    else:        # 공집합 즉 단조 증가가 하나도 없는 경우 -1 반환
        print(f"#{t} {-1}")