#01 모험가 길드 (이코테-그리디)
N = int(input())    #여행자 수 

member = list(map(int, input().split())) # 멤버리스트
a = [0 for _ in range(100001)]           # 공포도 리스트 
cnt = 0

for i in range(N):
    a[member[i]] += 1      #공포도 인덱스에 맞게 값을 추가


for i in range(1,100000):
    a[i+1] += a[i]%i     # 나머지를 뒤 인덱스에 추가
    cnt += a[i]//i

cnt += a[100000]//100000
    
print(cnt)
