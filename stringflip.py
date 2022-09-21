S = input()
cnt = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:  # 바뀌는 시점마다 카운트
        cnt += 1
print((cnt+1)//2)