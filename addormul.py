S = list(map(int, input()))

ans = 0
for ent in S:
    if ent <= 1 or ans <= 1:  # 0 or 1 혹은 ans 값이 1보다 작거나 같을경우
        ans += ent
    else:                    #나머지는 곱하기 
        ans *= ent

print(ans)


