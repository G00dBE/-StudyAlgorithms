def Pascal(n):     # 재귀함수 활용
    global memo
    if n>=2 and len(memo)<=n:
        list1 = Pascal(n-1)+[0]    # 이전 행 끝에 0 추가
        list2 = [0]+Pascal(n-1)    # 이전 행 앞에 0 추가
        memo.append([list1[i]+list2[i] for i in range(n)])  # 각 리스트를 더해 다음행만듦
    return memo[n]

memo = [0,[1]]

T = int(input())
    N = int(input())
    print(f"#{t+1}")
    for i in range(1,N+1):
        for ent in Pascal(i):
            print(str(ent), end=" ")
        print()
