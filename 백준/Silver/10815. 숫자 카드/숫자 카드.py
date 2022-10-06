import sys
input = sys.stdin.readline

N = int(input())
numcard = set(map(int, input().split()))

M = int(input())
lst = list(map(int, input().split()))

for i in range(M):
    if lst[i] in numcard:
        print(1,end=" ")
    else:
        print(0,end=" ")