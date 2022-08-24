for _ in range(1,11):
    tc = int(input())
    num = list(map(int, input().split())) #리스트 입력
    while num[-1]>0:  # 끝자리가 0이면 반복문 종료
        for i in range(5):  # 한사이클
            num[0] -= (i+1)
            if num[0] > 0:  # 0보다 클때는 그대로 추가
                num.append(num.pop(0))
            elif num[0] <= 0:  # 0보다 작을 때는
                num[0] = 0     # 0으로 값을 바꿔서 추가
                num.append(num.pop(0))
                break  # 반복문 종료
    print(f"#{tc}", end=" ")
    for ent in num:
        print(ent, end=' ')
    print()
