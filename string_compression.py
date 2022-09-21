# programmers 2020카카오 신입공채
# 문자열 압축
def solution(s):
    
    length_list = []
    t = 1
    
    while t <= len(s):
        tmp = ""
        cnt = 1 
        for i in range(0, len(s)-t, t):
            if s[i:i+t] == s[i+t:i+2*t]:
                cnt += 1
            else:
                if cnt != 1:
                    tmp += str(cnt)+s[i:i+t]
                    cnt = 1
                else:
                    tmp += s[i:i+t]
        remain = len(s)%t if len(s)%t else t
        if cnt != 1:
            tmp += str(cnt)+s[len(s)-remain:len(s)]
        else:
            tmp += s[len(s)-remain:len(s)]
        if len(tmp)<=len(s):
            length_list.append(len(tmp))
        t += 1
                         
    answer = min(length_list)
    return answer

print(solution("abcabcdede"))